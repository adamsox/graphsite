include<stdafx.h>

#include<iostream>

#include<conio.h>

using namespace std;

int s(int a[],int size,int num);

void main()

{ 
    int num,i;

    int a[7];

    for(i=0;i<=6;i++)

    { 
        cout<<" enter the number=";

        cin>>a[i];

    }

    cout<<"\n\t enter the required no=";

    cin>>num;

    int size=7;

    int save=s(a,size,num);

    if(save==-1)

    { 
        cout<<" not found ";

    }

    else

    {
        cout<<" found "<<a[save]<<" at location "<<save;

    }

    getch();

    int s(int a[],int size,int num)

    {
         int mid,low,high;

        high=size-1;

        low=0;

        mid=size/2;

        while(low!=high)

        { 
            if(a[mid]==num)

            { return mid; }

            else

            { if (a[mid]>num)

            { high=mid-1; }

            else

            { low=mid+1; }

            }

            mid=(low+high)/2;

        }

    if (a[mid]==num)

    { 
        return mid;
    }

    else

    { 
        return-1; 
    }

}