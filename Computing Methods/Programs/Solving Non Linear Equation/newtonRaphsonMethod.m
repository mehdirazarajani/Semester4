format short;
str=input('Type the equation in terms of x: ','s');
str1=input('Type the derivative of equation in terms of x: ','s');
y=input('Enter the initial guess:\n');
f=inline(str,'x');
df=inline(str1,'x');
valA=feval(f,y);
TOL=input('Enter the value of TOL:\n');

check = true;
val = feval(f,y);
   if abs(val) <= TOL;
       fprintf('f(%f) = %f\n',y,val);
       display('succeded');
       check = false;
   end
   if check
        fprintf('f(%f) = %f\n',y,val);
   end
while check;
   valY = feval(f,y);
   valD = df(y);
   newY = y - valY/valD;
   newVal = feval(f,newY);
   if abs(newVal) <= TOL
       fprintf('ANS = %f\n',newY);
       display('succeded');
       break;
   end
   error = abs((y-newY)/y);
   fprintf('f(%f) = %f\t\terror = %f\n',newY,f(newY),error);
   y = newY;
   if error <= TOL
       fprintf('ANS = %f\n',newY);
       display('succedded');
       break;
   end
end