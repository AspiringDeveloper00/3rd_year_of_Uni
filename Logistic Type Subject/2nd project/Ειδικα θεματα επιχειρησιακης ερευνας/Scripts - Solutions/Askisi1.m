%% Solutions of subproblems with the branch and bound algorithm
clc
clear

%My AM sum was 18=1+8+0+6+3
%Lower bounds and objective function always the same
f=[8;6];
lb=zeros(2,1);

%1st linear problem
a1=[-2 -2
    -4.5 -1
    1 2];
b1=[9;-28;10];
[x1,fval1,exitflag1,output1,lambda1] = linprog(f,a1,b1,[],[],lb);

%2nd linear problem
a2=[-2 -2
    -4.5 -1
    1 2
    1 0];
b2=[9;-28;10;6];
[x2,fval2,exitflag2,output2,lambda2] = linprog(f,a2,b2,[],[],lb);

%3nd linear problem
a3=[-2 -2
    -4.5 -1
    1 2
    -1 0];
b3=[9;-28;10;-7];
[x3,fval3,exitflag3,output3,lambda3] = linprog(f,a3,b3,[],[],lb);
