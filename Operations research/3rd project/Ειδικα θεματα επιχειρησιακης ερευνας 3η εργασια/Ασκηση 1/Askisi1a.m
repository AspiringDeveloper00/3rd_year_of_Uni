%% Bisection search method 
% AM=P18063 -->  1*x^5 - 8*x^4 + 0*x^3 - 6*x^2 + 3

% Equation: f(x) = x^5 - 8*x^4 - 6*x^2 + 3
% Derivative: F=f'(x) = 5*x^4-32*x^3-12*x

F =@(x) (1*x.^5)-(8*x.^4)-(6*x^2)+3; % given function
f=@(x) (5*x.^4)-(32*x.^3)-(12*x); % derivative 
e = 10^(-6);
a = -10;
b = 10;

while ( b-a>=0||(abs(f(a))>=e && abs(f(b))>=e) )
    c=(a+b)/2;
    if (f(c)==0)
        break;
    elseif (f(a)*f(c)< 0)
        b=c;
    else
        a=c;
    end
end

fprintf("Using the bisection search method, the local max value of f(x)= x^5 - 8*x^4 - 6*x^2 + 3 in [-10,10] with an e=10^-6 is the point: ("+c+","+F(c)+")")


