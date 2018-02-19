format short;
str=input('Type the equation in terms of x: ','s');
y0=input('Enter the first interval:\n');
f=inline(str,'x');
val0=feval(f,y0);
y1=input('Enter the second interval:\n');
val1=feval(f,y1);
TOL=input('Enter the value of TOL:\n');

check = true;
   if val0 == 0;
       fprintf('f(%f) = %f\n',y0,val0);
       display('succeded');
       check = false;
   end
   if not(check) && val1 == 0;
       fprintf('f(%f) = %f\n',y1,val1);
       display('succeded');
       check = false;
   end
error = abs((y0-y1)/y0);
   if not(check) && error <= 0.00001 ;
       fprintf('f(%f) = %f\n',y1,val1);
       display('succeded');
       check = false;
   end
   if check
        fprintf('f(%f) = %f\n',y0,val0);
        fprintf('f(%f) = %f\n',y1,val1);
   end
while check;
    temp = (y0*val1-y1*val0)/(val1-val0);
    y0 = y1;
    y1 = temp;
    val0 =val1;
    val1 = feval(f,temp);
   if abs(val1) <= TOL;
       fprintf('ANS = %f\n',y1);
       display('succeded');
       break;
   end
   error = abs((y0-y1)/y0);
   fprintf('f(%f) = %f\t\terror = %f\n',y1,val1,error);
   if error <= TOL;
       fprintf('ANS = %f\n',y1);
       display('succedded');
       break;
   end
end