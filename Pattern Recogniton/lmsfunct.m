%% LMS algorithm function 
function total=lmsfunct(betarray,r,numRows)

% For 10-fold-cross validation we create an array of 11 indexes. The
% distance between these 11 indexes is the 10% of the number of the total
% data (matches). Each pair (1-2,2-3,etc) represent the first and last
% index of the rows that will be tested.For example if we have 100 matches
% this fold-cross-limits table will be like [1,10,20,..,100], 1 through 10
% being the first set of data to be tested, 10 through 20 the second set
% etc.
percent=int16(numRows*(10/100));
fold_Cross_limits=ones(1,11);
accarray=zeros(1,10);

for j=1:10
    if j~=10
        fold_Cross_limits(j+1)=percent*j;
    else
        fold_Cross_limits(j+1)=numRows; 
    end
end



for j=1:10
    
    % TRAINING
    % for each one of the 10 fold-cross-validation we initialize the weight matrix and the 
    %learning rate (variable a)(because the learning rate is becoming smaller for each
    %iteration so that the error can be minimized and the weight matrix stops getting updated).  
    w=[0,0,0,0;0,0,0,0;0,0,0,0;];
    k=1;
    a=0.5;
    for i= 1:numRows
        %if the data are not in the testing set --> then update the weight matrix according to the LMS algorithm 
        if i<fold_Cross_limits(j)|| i>fold_Cross_limits(j+1) 
            w(1,1)=w(1,1)+a*betarray(i,1)*(r(i,1) -(betarray(i,1)'* w(1,1)));
            w(1,2)=w(1,2)+a*betarray(i,2)*(r(i,1) -(betarray(i,2)'* w(1,2)));
            w(1,3)=w(1,3)+a*betarray(i,3)*(r(i,1) -(betarray(i,3)'* w(1,3)));
            w(1,4)=w(1,4)+a*betarray(i,4)*(r(i,1) -(betarray(i,4)'* w(1,4)));

            w(2,1)=w(2,1)+a*betarray(i,1)*(r(i,2) -(betarray(i,1)'* w(2,1)));
            w(2,2)=w(2,2)+a*betarray(i,2)*(r(i,2) -(betarray(i,2)'* w(2,2)));
            w(2,3)=w(2,3)+a*betarray(i,3)*(r(i,2) -(betarray(i,3)'* w(2,3)));
            w(2,4)=w(2,4)+a*betarray(i,4)*(r(i,2) -(betarray(i,4)'* w(2,4)));

            w(3,1)=w(3,1)+a*betarray(i,1)*(r(i,3) -(betarray(i,1)'* w(3,1)));
            w(3,2)=w(3,2)+a*betarray(i,2)*(r(i,3) -(betarray(i,2)'* w(3,2)));
            w(3,3)=w(3,3)+a*betarray(i,3)*(r(i,3) -(betarray(i,3)'* w(3,3)));
            w(3,4)=w(3,4)+a*betarray(i,4)*(r(i,3) -(betarray(i,4)'* w(3,4)));
            a=a/k;
            k=k+1;
        end
    end
    %TESTING
    %test the data that are each time in the testing set according to the following multiplication:data x weight matrix.
    %Each result will be ofthe format of [0.7,0.2,0.5].We make the max value equal to one and the rest equal to zero so
    %we will have a matrix: [1,0,0]. We now check if the predicted outcome is the same as the actual outcome and if it is
    %count it.Then we divide the number of the succesufull predictions with the number of tested data.We do the above
    %10 times for each interation of the 10-fold-cross-validation.Finally we find the average of the above 10 accuracies
    %and this will be the final accuracy of the betting company.  
    index=1;
    tmptesting=zeros(fold_Cross_limits(j+1)-fold_Cross_limits(j)+1,3);
    for z=fold_Cross_limits(j):fold_Cross_limits(j+1)
        tmptesting(index,:)=betarray(z,:)*w';
        max=-1;
        for tmp=1:3
            if tmptesting(index,tmp)>max
                max=tmptesting(index,tmp);
            end
        end
        for tmp=1:3
            if tmptesting(index,tmp)==max
                tmptesting(index,tmp)=1;
            else
                tmptesting(index,tmp)=0;
            end
        end
        index=index+1;
    end
    index=1;
    acc=0;
    for z=fold_Cross_limits(j):fold_Cross_limits(j+1)
        if tmptesting(index,:)==r(z,:)
            acc=acc+1;
        end
        index=index+1;
    end
    accarray(j)=acc/(fold_Cross_limits(j+1)-fold_Cross_limits(j)+1);
end
total=0;
for i=1:10
    total=total+accarray(j);
end
total=(total*10);
end