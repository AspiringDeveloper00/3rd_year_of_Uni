%% Newton - Raphson method
% AM=P18063 -->  1*x^5 - 8*x^4 + 0*x^3 - 6*x^2 + 3

% Equation: f(x) = x^5 - 8*x^4 - 6*x^2 + 3
% Derivative: F=f'(x) = 5*x^4-32*x^3-12*x

f= (5*x.^4)-(32*x.^3)-(12*x); % given function
g=diff(f); % derivative 
e = 10^(-6);

while (true)
    x0 = input('Enter an intial approximation x0:');
    if (x0~=0)
        break;
    end
    fprintf('x0 must not be equal to 0');
    fprintf('\n');
end

for i=1:100 %100 iterations is enough
    f0=vpa(subs(f,x,x0)); %value of function at x0
    f0_der=vpa(subs(g,x,x0)); %value of function derivative at x0
    y=x0-f0/f0_der; % The Formula
    err=abs(y-x0);
    if err<e %checking the error at each iteration
        break;
    end
    x0=y;
end
y = y - rem(y,10^-6); %Displaying upto required decimal places
F =@(x) (1*x.^5)-(8*x.^4)-(6*x^2)+3;
fprintf("Using the Newton - Raphson method after %d iterations that, the local max value of f(x)= x^5 - 8*x^4 - 6*x^2 + 3 with an e=10^-6 is the point: (%f,%f)",i,y,F(y))