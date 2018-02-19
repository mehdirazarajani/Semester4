format short;
str=input('Type the equation in terms of x: ','s');
y=input('Enter the initial guess:\n');
f=inline(str,'x');
val=feval(f,y);
TOL=input('Enter the value of TOL:\n');

check = true;
val=feval(f,y);
   if val == 0;
       fprintf('f(%f) = %f\n',y,val);
       display('succeded');
       check = false;
   end
while check;
    newVal = feval(f,val);
    if abs(val) <= TOL;
       fprintf('ANS = %f\n',val);
       display('succeded');
       break;
    end
   error = abs((val-newVal)/val);
   fprintf('f(%f) = %f\t\terror = %f\n',val,newVal,error);
   if val == newVal
       fprintf('ANS = %f\n',val);
       display('succedded');
       break;
   elseif error < TOL;
       fprintf('ANS = %f\n',val);
       display('succedded');
       break;
   end
   val = newVal;
end