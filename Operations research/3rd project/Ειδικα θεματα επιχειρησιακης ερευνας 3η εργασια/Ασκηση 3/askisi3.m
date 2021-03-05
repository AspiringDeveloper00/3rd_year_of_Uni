%% Lagrange method

%Min f(x,y)=x^2 + 18y^2
%g(x,y) = 18x + 18y - 18 ----> g(x,y) = x + y - 1
%L(x,y,λ)=f(x,y)+λ*g(x,y)

syms x y l

f=x^2 + 18*y^2;
g= x + y - 1;

L=f+ l*g;

disp("My function according to my AM=18063: f="+string(f))
disp("My constraint according to my AM=18063: g="+string(g))
disp("My Lagrange function: L="+string(L))
disp(" ")

eqnx=diff(L,x);
eqny=diff(L,y);
eqnl=diff(L,l);
disp("Derivatives dL/dx, dL/dy, dL/dl: "+string(eqnx)+" , "+string(eqny)+" , "+string(eqnl))
disp(" ")

hess=hessian(L);
disp("Hessian matrix:")
disp(hess)
disp(" ")

disp("Leading principal minors to be examined: n-m=2-1=1 where n is the number of variables(x,y) and m the number of constraints")
disp("The determinant is:"+string(det(hess))+"so it follows the rule (-1)^m, where m=1. So the following point (x,y) is the local minimum")

[A,B] = equationsToMatrix([eqnx, eqny,eqnl], [x, y,l]);
X = linsolve(A,B);
x=X(1);
y=X(2);
l=X(3);
disp(x)
disp(y)

