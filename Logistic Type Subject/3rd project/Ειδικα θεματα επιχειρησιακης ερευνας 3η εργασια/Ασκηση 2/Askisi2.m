%% Max of f(x)

%f(x,y)=-6y-x^2+3xy-y^2
disp(" ")

syms x y 
f=-6*y-x^2+3*x*y-y^2;

disp("My function according to my AM=18063: f="+string(f))
disp(" ")

eqn=jacobian(f);
disp("Derivatives found with jacobian() function: "+string(eqn(1))+" , "+string(eqn(2)))
disp(" ")

hess=hessian(f);
disp("Hessian matrix:")
disp(hess)
disp(" ")

[A,B] = equationsToMatrix([eqn(1), eqn(2)], [x, y]);
X = linsolve(A,B);
x=X(1);
y=X(2);

disp("Essential condition in order for a extremum to exist is the 2 derivatives of the jacobian table to have a common x0 that: f'1(x0)=0 and f'2(x0)=0. These coordinates are the following: ("+string(x)+","+string(y)+")")
disp("Checking if the above is a local extremum...")
disp("------------------------------Eigenvalues Method------------------------------")
disp("The eigenvalues of the hessian matrix are ")
disp(eig(hess))
disp("Because the 2 eigenvalues have different sign (-5,+ 1) the point under investigation is a saddle point")
disp(" ")
disp("------------------------------Sylvester's Method------------------------------")
disp("Leading principal minors: ")
disp(det(hess(1,1)))
disp(det(hess))
disp("Principal minors: ")
disp("First rank")
disp(det(hess(1,1)))
disp(det(hess(1,2)))
disp(det(hess(2,1)))
disp(det(hess(2,2)))
disp("Second rank")
disp(det(hess))
disp("Leading principal minors are not all positive numbers neither they change sign based on the following rule: (-1)^k*Dk>0 where k is the rank")
disp("Principal minors are not all non-negative neither they change sign based on the following rule: (-1)^k*Dk>=0 where k is the rank")
disp("We can see that the none of the 4 conditions of Sylvester's criteria is met, so we confirm that we are dealing with a saddle point")

