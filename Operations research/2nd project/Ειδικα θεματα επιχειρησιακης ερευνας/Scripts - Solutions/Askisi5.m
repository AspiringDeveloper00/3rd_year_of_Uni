%% Solutions of subproblems with the branch and bound algorithm
clc
clear


f=[4;3;2;0;0;0];
lb=zeros(6,1);
ub= [Inf;Inf;Inf;1;1;1];
intcon = [1:6];
M=10000;

a1=[3.5,1.5,2.5,0,0,0
    32,34,36,0,0,0 
    1,0,0,-M,0,0 
    -1,0,0,M,0,0 
    0,1,0,0,-M,0
    0,-1,0,0,-M,0 
    0,0,1,0,0,-M
    0,0,-1,0,0,-M];

b1=[6500;65000;0;-1000+M;0;-1000+M;0;-1000+M];

[x,fval,exitflag,output] = intlinprog(-f,intcon,a1,b1,[],[],lb,ub);
