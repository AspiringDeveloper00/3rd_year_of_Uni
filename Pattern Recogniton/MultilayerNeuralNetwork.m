%% Multilayer neural network


%Fetch in tmpx the data of the team attributes, setting a matrix of zeros
%in which the data of the team attributes and bets of each betting company
%will be stored. This will be a matrix of 22309x28 where 8 plus 8 the team
%attributes of the 2 teams plus 4 times 3 the 3 bets of each of the 4
%companies. There will be less than 22592 matches(like it used to be in the
%first 2 algorithms) because some teams have no team attributes data.

tmpx=[TeamAttributes(:,3),TeamAttributes(:,5),TeamAttributes(:,7),TeamAttributes(:,10),TeamAttributes(:,12),...
    TeamAttributes(:,14),TeamAttributes(:,17),TeamAttributes(:,19),TeamAttributes(:,21)];
rows = height(Match);
xtable=zeros(rows,28);
tmpx.team_api_id=categorical(tmpx.team_api_id);

%Initializing the one hot vector encoded table with the matches' outcome.
%100 for home win, 010 for a draw, 001 for an away win.
r=zeros(rows,3); 
  goals=table2array([Match(:,10),Match(:,11)]);
for i=1:rows
    if goals(i,1)>goals(i,2)
        r(i,1)=1;
        r(i,2)=0;
        r(i,3)=0;
    elseif goals(i,1)<goals(i,2)
        r(i,1)=0;
        r(i,2)=0;
        r(i,3)=1;
    else
        r(i,1)=0;
        r(i,2)=1;
        r(i,3)=0;
    end
end

%For each match...
for i=1:rows
    %...fetch the ids of the wanted teams (home,away)...
    home=string(table2array(Match(i,8)));
    away=string(table2array(Match(i,9)));
    
    %...and use them to find their team attributes data...
    homes=tmpx(tmpx.team_api_id == home,:);
    aways=tmpx(tmpx.team_api_id == away,:);
    
    %...and if one of the teams has no attributes set the whole row equal
    %to zero for the xtable(final data table) and the r table(encoded
    %scores table)...
    if height(homes)==0 || height(aways)==0
         xtable(i,:)=zeros(1,28);
         r(i,:)=zeros(1,3);
    else
        %...however if both teams have attribute data, if the data are
        %multiple(different for each year or season), take the average of
        %them. From 1 to 8 column will be the home team's attributes, from
        %9 to 16 column will be the away team's attributes and from 17 to
        %28 will be the 12 bets (3 for each of the 4 companies)
        xtable(i,1:8)=mean(table2array(homes(:,2:9)));
        xtable(i,9:16)=mean(table2array(aways(:,2:9)));
        xtable(i,17:28)=double(table2array(Match(i,12:23)));
    end
end

%Delete the rows of zeros(because there was not any team attributes for the
%competing team or teams.
r( ~any(r,2), : ) = []; 
xtable( ~any(xtable,2), : ) = []; 

% counting the number of Home wins and Away wins and draws
tmp=sum(r);
numH=tmp(1);
numD=tmp(2);
numA=tmp(3);

[rows,cols] = size(r);


homewinsclass=zeros(numH,28);
drawclass=zeros(numD,28);
awaywinsclass=zeros(numA,28);


% Creating 3 matrices home win, draw and away win each one having 28 vector
% attributes.
index1=1;
index2=1;
index3=1;
for i=1:rows
    if r(i,1)==1
        homewinsclass(index1,:)=xtable(i,:);
        index1=index1+1;
    elseif r(i,2)==1
        drawclass(index2,:)=xtable(i,:);
        index2=index2+1;
    elseif r(i,3)==1 
        awaywinsclass(index3,:)=xtable(i,:);
        index3=index3+1;
    end        
end

TRAINPERCENT=60;

%Creating 3 matrices for the 3 different training
%classes(home,draw,away),submatrices of homewinsclass,drawclass,awaywinsclass
trainhome=homewinsclass(1:int16(numH*(TRAINPERCENT/100)),:);
traindraw=drawclass(1:int16(numD*(TRAINPERCENT/100)),:);
trainaway=awaywinsclass(1:int16(numA*(TRAINPERCENT/100)),:);

%Creating 3 matrices for the 3 different testing 
%classes(home,draw,away),submatrices of homewinsclass,drawclass,awaywinsclass
testhome=homewinsclass(int16(numH*(TRAINPERCENT/100))+1:numH,:);
testdraw=drawclass(int16(numD*(TRAINPERCENT/100))+1:numD,:);
testaway=awaywinsclass(int16(numA*(TRAINPERCENT/100))+1:numA,:);

% Set the training patterns matrix for the feed forward neural network object.
P = [trainhome;traindraw;trainaway];
P = P';

% Set the target vector corresponding to the training patterns stored in P.
T = [ones(1,int16(numH*(TRAINPERCENT/100))),2*ones(1,int16(numD*(TRAINPERCENT/100))),...
    3*ones(1,int16(numA*(TRAINPERCENT/100)))];
T = full(ind2vec(T));

% Set the neural network
net = newff(P,T,[6 3 3],{'tansig' 'tansig' 'tansig'});
init(net);
net.trainParam.epochs = 200;
net.trainParam.showCommandLine = 1;
net.trainParam.goal = 0.00001;
net.trainParam.lr = 0.01;
net.trainFcn = 'trainbr';
net = train(net,P,T);

[~,c]=size(T);
% Check network performance on training patterns.
EstimatedTrainingTargets = sim(net,P);
EstimatedTrainingTargets = round(EstimatedTrainingTargets);
Differences = abs(EstimatedTrainingTargets - T);
CorrectTrainClassificationRatio = 1 - (sum(Differences) / c);


% Set the testing patterns matrix for the feed forward neural network object.
P = [testhome;testdraw;testaway];
P = P';

% Set the target vector corresponding to the testing patterns stored in P.
T = [ones(1,numH-int16(numH*(TRAINPERCENT/100))),2*ones(1,numD-int16(numD*(TRAINPERCENT/100))),...
    3*ones(1,numA-int16(numA*(TRAINPERCENT/100)))];
T = full(ind2vec(T));

[~,c]=size(T);
% Check network performance on testing patterns.
EstimatedTestingTargets = sim(net,P);
EstimatedTestingTargets = round(EstimatedTestingTargets);
Differences = abs(EstimatedTestingTargets - T);
CorrectTestClassificationRatio = 100*(1 - (sum(sum(Differences)) / c));

disp("The correct test classification ratio is: "+CorrectTestClassificationRatio+"%")