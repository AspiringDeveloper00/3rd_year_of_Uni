%% Data extraction

%extracting the four betting companies tables of format(dh,dd,da) and
%adding 1 column of 1s(ones) for the bias term.New format will be
%(dh,dd,da,1).


xbet365=cat(2,double(table2array([Match(:,12),Match(:,13),Match(:,14)])),ones(22592,1));
xbw=cat(2,double(table2array([Match(:,15),Match(:,16),Match(:,17)])),ones(22592,1));
xiw=cat(2,double(table2array([Match(:,18),Match(:,19),Match(:,20)])),ones(22592,1));
xlb=cat(2,double(table2array([Match(:,21),Match(:,22),Match(:,23)])),ones(22592,1));

%extracting the score tables of format (1-2,2-3 etc.) and making it of the
%format of (100 if Home wins,010 if Draw, 001 if Away wins). These scores
%are stored in an array named r,of the size x=number of matches and y=3.
goals=table2array([Match(:,10),Match(:,11)]);

%getting the numbers of matches
[numRows,numCols] = size(goals);

r=zeros(numRows,3); 

%counting the number of Home wins and Away wins 
numH=0;
numD=0;
numA=0;
for i=1:numRows
    if goals(i,1)>goals(i,2)
        r(i,1)=1;
        r(i,2)=0;
        r(i,3)=0;
        numH=numH+1;
    elseif goals(i,1)<goals(i,2)
        r(i,1)=0;
        r(i,2)=0;
        r(i,3)=1;
        numA=numA+1;
    else
        r(i,1)=0;
        r(i,2)=1;
        r(i,3)=0;
        numD=numD+1;
    end
end

%% Data visualization for betting companies using 4 different figures
% Initializing 3 different empty arrays for each company,one for the Home
% wins,one for the Draws and one for the Away wins, containing the
% coordinates x,y,z where x=dh y=dd z=da 
xbet365H=zeros(numH,3);
xbet365D=zeros(numD,3);
xbet365A=zeros(numA,3);
 
xbwH=zeros(numH,3); 
xbwD=zeros(numD,3);
xbwA=zeros(numA,3);

xiwH=zeros(numH,3);
xiwD=zeros(numD,3);
xiwA=zeros(numA,3);

xlbH=zeros(numH,3);
xlbD=zeros(numD,3);
xlbA=zeros(numA,3);

for i=1:numRows
    if r(i,1)==1
        xbet365H(i,:)=xbet365(i,1:3);
        xbwH(i,:)=xbw(i,1:3);
        xiwH(i,:)=xiw(i,1:3);
        xlbH(i,:)=xlb(i,1:3);
    elseif r(i,2)==1
        xbet365D(i,:)=xbet365(i,1:3);
        xbwD(i,:)=xbw(i,1:3);
        xiwD(i,:)=xiw(i,1:3);
        xlbD(i,:)=xlb(i,1:3);
    elseif r(i,3)==1 
        xbet365A(i,:)=xbet365(i,1:3);
        xbwA(i,:)=xbw(i,1:3);
        xiwA(i,:)=xiw(i,1:3);
        xlbA(i,:)=xlb(i,1:3);
    end        
end


x1=xbet365H(:,1);
y1=xbet365H(:,2);
z1=xbet365H(:,3);

x2=xbet365D(:,1);
y2=xbet365D(:,2);
z2=xbet365D(:,3);

x3=xbet365A(:,1);
y3=xbet365A(:,2);
z3=xbet365A(:,3);

figure("Name","B365 H-D-A Plot",'NumberTitle','off')
scatter3(x1, y1, z1, 'r', 'filled')
hold on
scatter3(x2, y2, z2, 'y', 'filled')
scatter3(x3, y3, z3, 'b', 'filled')
hold off
grid on
xlabel('d(H)')
ylabel('d(D)')
zlabel('d(A)')
legend('Home wins', 'Draws','Away wins')

x1=xbwH(:,1);
y1=xbwH(:,2);
z1=xbwH(:,3);

x2=xbwD(:,1);
y2=xbwD(:,2);
z2=xbwD(:,3);

x3=xbwA(:,1);
y3=xbwA(:,2);
z3=xbwA(:,3);

figure("Name","BW H-D-A Plot",'NumberTitle','off')
scatter3(x1, y1, z1, 'r', 'filled')
hold on
scatter3(x2, y2, z2, 'y', 'filled')
scatter3(x3, y3, z3, 'b', 'filled')
hold off
grid on
xlabel('d(H)')
ylabel('d(D)')
zlabel('d(A)')
legend('Home wins', 'Draws','Away wins')

x1=xiwH(:,1);
y1=xiwH(:,2);
z1=xiwH(:,3);

x2=xiwD(:,1);
y2=xiwD(:,2);
z2=xiwD(:,3);

x3=xiwA(:,1);
y3=xiwA(:,2);
z3=xiwA(:,3);

figure("Name","IW H-D-A Plot",'NumberTitle','off')
scatter3(x1, y1, z1, 'r', 'filled')
hold on
scatter3(x2, y2, z2, 'y', 'filled')
scatter3(x3, y3, z3, 'b', 'filled')
hold off
grid on
xlabel('d(H)')
ylabel('d(D)')
zlabel('d(A)')
legend('Home wins', 'Draws','Away wins')

x1=xlbH(:,1);
y1=xlbH(:,2);
z1=xlbH(:,3);

x2=xlbD(:,1);
y2=xlbD(:,2);
z2=xlbD(:,3);

x3=xlbA(:,1);
y3=xlbA(:,2);
z3=xlbA(:,3);

figure("Name","LB H-D-A Plot",'NumberTitle','off')
scatter3(x1, y1, z1, 'r', 'filled')
hold on
scatter3(x2, y2, z2, 'y', 'filled')
scatter3(x3, y3, z3, 'b', 'filled')
hold off
grid on
xlabel('d(H)')
ylabel('d(D)')
zlabel('d(A)')
legend('Home wins', 'Draws','Away wins')

%% Running the Lms and Mse algorithms for each one of the 4 companies 
disp("LMS algorithm with 10 fold cross validation and one hot vector encoding")

total=lmsfunct(xbet365,r,numRows);
disp("B365 accuracy "+total+"%")
maxb="B365";
maxa=total;

total=lmsfunct(xbw,r,numRows);
disp("BW accuracy "+total+"%")
if total>maxa
    maxb="BW";
    maxa=total;
end

total=lmsfunct(xiw,r,numRows);
disp("IW accuracy "+total+"%")
if total>maxa
    maxb="IW";
    maxa=total;
end

total=lmsfunct(xlb,r,numRows);
disp("LB accuracy "+total+"%")
if total>maxa
    maxb="LB";
    maxa=total;
end

disp("The most accurate betting company with the lms algorithm was "+maxb+" with an accuracy of "+maxa+"%")

disp(" ")

disp("MSE algorithm with 10 fold cross validation and one hot vector encoding")

total=msefunct(xbet365,r,numRows);
disp("B365 accuracy "+total+"%")
maxb="B365";
maxa=total;

total=msefunct(xbw,r,numRows);
disp("BW accuracy "+total+"%")
if total>maxa
    maxb="BW";
    maxa=total;
end

total=msefunct(xiw,r,numRows);
disp("IW accuracy "+total+"%")
if total>maxa
    maxb="IW";
    maxa=total;
end

total=msefunct(xlb,r,numRows);
disp("LB accuracy "+total+"%")
if total>maxa
    maxb="LB";
    maxa=total;
end

disp("The most accurate betting company with the mse(ls) algorithm was "+maxb+" with an accuracy of "+maxa+"%")
