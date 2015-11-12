#include<iostream>
#include<cmath>
using namespace std;
int main()
{
long double N;
cin>>N;
double MAX=1;
long double D=N;
long double temp1,temp2;
long double Dval=0;
while(D>1.0)
    {

        if (sqrt(D)==int(sqrt(D)))
           {
            D-=1;

            continue;
           }
        else
           {
            while (){
        //            cout<<sqrt((x*x-1.0)/D)<<"Stuck here"<<endl;
            //cout<<1;
            counter+=1;
            if (counter>=20000)
                break;
            x+=1;
            }
      //      cout<<sqrt((x*x-1.0)/D)<<"Stuck here"<<endl;
            if(x>MAX)
            {
                MAX=x;
                Dval=D;
            }
           }

    D--;
    //cout<<D<<'p';
    }

cout<<Dval;
return 0;
}
