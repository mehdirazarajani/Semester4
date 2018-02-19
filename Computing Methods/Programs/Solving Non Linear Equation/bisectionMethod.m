format short;
str=input('Type the equation in terms of x: ','s');
a=input('Enter the first interval:\n');
f=inline(str,'x');
valA=feval(f,a);
b=input('Enter the second interval:\n');
valB=feval(f,b);
TOL=input('Enter the value of TOL:\n');

check = true;
if abs(valA) <= TOL
     fprintf('f(%f) = %f\n',a,valA);
     display('succeded');
     check = false;
elseif abs(valB) <= TOL
     fprintf('f(%f) = %f\n',b,valB);
     display('succeded');
     check = false;
elseif not((valA>0 && valB<0)||(valB>0 && valA<0))
    display('Answer is not in the given rannge');
    check = false;
end
n = 1;
while check
    error = abs(a-b)/2^n;
    n = n+1;
    if error <= TOL
        fprintf('ANS f(%f) = %f\n',c,valC);
        display('suceeded');
        check = false;
    end
    fprintf('f(%f) = %f\tf(%f) = %f\t\t\terror = %f\n',a,valA,b,valB,error);
    c = (a + b)/2;
    valC=feval(f,c);
    if abs(valC) <= TOL
        fprintf('ANS f(%f) = %f\n',c,valC);
        display('succeded');
        check = false;
    elseif valC > 0
        if valA > 0
            a = c;
            valA = valC;
        else
            b = c;
            valB = valC;
        end
    else
        if valA < 0
            a = c;
            valA = valC;
        else
           b = c;
           valB = valC;
        end
    end
end