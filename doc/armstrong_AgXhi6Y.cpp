#include<iostream>
using namespace std;
int main()
{
    int i,a,r,c,p=0;
    cout<<"enter a num";
    cin>>c;
    a=c;
    i=1;
    do
    {
        r=a%10;
        a=a/10;
        p=p+(r*r*r);
    }
    while(a>0);
      if(p==c)
      {
          cout<<"num is armstrong";
      }
      else
      {
          cout<<"not";
      }
    }

