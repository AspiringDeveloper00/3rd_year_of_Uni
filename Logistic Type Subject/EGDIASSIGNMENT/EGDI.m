%% EGDI 
clear
clc

%%Load data from xls
data=xlsread('EGDI_DATA_2020','Data','B2:D176');
[n,m]=size(data);

epsilon=10^-6;
 
%% Model M1/1st scenario
m1=zeros(n,1);

%Lower Bounds 
lb1=[epsilon*ones(1,m)];

for i=1:n
    
    f=[-data(i,1:m)]; %Objective function
    a=data(:,1:m); % Left Hand Side of Constraints (𝑢𝑌𝑗)
    b=ones(1,n); % Right Hand Side of Constraints (1)
    
    
   [z,fval,exitflag,output] = linprog(f,a,b,[],[],lb1);
   m1(i,1)= -fval;
end


 %% Model M4/2nd scenario
 m4=zeros(n,1);
 
 %Lower Bounds 
 lb4=[epsilon*ones(1,m) zeros(1,n)];
 
 f=[zeros(1,m) ones(1,n)]; %Objective function
 a=[data(:,1:m) eye(n)]; % Left Hand Side of Constraints (𝑢𝑌𝑗 + 𝑑𝑗)
 b=ones(1,n); % Right Hand Side of Constraints (1)
 
 
 [z,fval,exitflag,output] = linprog(f,[],[],a,b,lb4); 
 
 for i=1:n
    m4(i,1)= data(i,1:m) * z(1:m);
 end
 
 %% Model M6/3rd scenario
 m6=zeros(n,1);
 
 %Lower Bounds 
 lb6=[epsilon*ones(1,m) 0];
 
 f=[zeros(1,m) 1]; %Objective function (δ is -1 because lp_solve is maximization problem)
 a=[-data(:,1:m) -ones(n,1); data(:,1:m) zeros(n,1)];% Left Hand Side of Constraints (𝑢𝑌𝑗 + δ ; 𝑢𝑌𝑗 + 0) (
 b=[-ones(1,n) ones(1,n)]; % Right Hand Side of Constraints (1 ; 1)
 
 [z,fval,exitflag,output] = linprog(f,a,b,[],[],lb6); 
 
 for i=1:n
    m6(i,1)= data(i,1:m)* z(1:m);
 end
 
 %% Model M6/4rd scenario
 
 m6_4=zeros(n,1);
 
 %Lower Bounds 
 lb6_4=[epsilon*ones(1,m) 0];
 
 f=[zeros(1,m) 1]; %Objective function (δ is -1 because lp_solve is maximization problem)
 a=[-data(:,1:m) -ones(n,1); data(:,1:m) zeros(n,1); -1 0 2 0 ; -1 3 0 0 ];% Left Hand Side of Constraints (𝑢𝑌𝑗 + δ ; 𝑢𝑌𝑗 + 0 ; u1-2u3 ; u1-3u2 )
 b=[-ones(1,n) ones(1,n) 0 0]; % Right Hand Side of Constraints (1 ; 1 ; 0 ; 0)
 
 
 [z,fval,exitflag,output] = linprog(f,a,b,[],[],lb6_4);
 
 for i=1:n
    m6_4(i,1)= data(i,1:m)* z(1:m);
 end
 
 
