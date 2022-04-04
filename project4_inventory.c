
#include <stdio.h>
#include <stdlib.h>

// Adam Bricha (U9233-5585) This program takes user input for an array of elements, then uses the function find_minimum to find how many computers the factory can build.
// The program looks for duplicates using pointers and finds the least amount of duplicates and prints it to the user.


int find_minimum(int *a, int n)
{  

int *p =a;    //points to first element of the array
int min = *a;  //sets min to the first element of the array

for(p=a; p<a+n; p++){   //runs through the array and finds the minimum value pointed by p
    if (*p < min){
    min = *p;

}
}

return min;  // returns the minimum value pointed by p
}

int main()
{

int N;  // Number of parts
int K;  // Number of part types
int parts;

printf("Enter number of parts (N): ");
scanf("%d",&N);


if (N<1 || N>1000000){    //input validaiton
    printf("Must be in the range [1,1000000]");
    exit(0);
}

printf("\nEnter number of part types (K): ");
scanf("%d",&K);

if (K<1 || K>10000){     //input validation
    printf("Must be in the range [1,10000]");
    exit(0);
}

int a[K];   // intializes array and sets it to length K

int i =0;        //Counter so code doesnt mess up in student cluster
while(i<K){  
    a[i]=0;
    i++;
}
    
printf("\nEnter Part list: \n");    // gets list of parts
for(int j=0;j<N;j++){
    scanf("%d",&parts);
    if (parts > K || parts <1 ){
        printf("invalid list of parts. Parts code must be in range [1,%d]", K);
        exit(0);
    }
    a[parts-1] += 1;
    }


int result = find_minimum(a,K);  //calls function
printf("The factory can build %d computer(s)",result);   //returns result
}
