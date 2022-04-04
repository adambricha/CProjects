

#include <stdio.h>

// Adam Bricha (U9233-5585). This program takes an array of elements and calls the function find_parity to find out if the elements are all even or all odd or nethier.
// The program uses pointers, arrays, functions and forloops

void find_parity(int *a, int n, int *all_even, int *all_odd){  //function defined to see if elements are all even or all odd

int *p = a; //set pointer to first element of array

    for(p=a; p<a+n; p++){       // loops through element of each array
        if(*p%2 == 0){           // check if even by using mod
            *all_even=1;             
        }
        else if(*p%2 == 1)      //check if odd by using mod
            *all_odd = 1;
        
    }


}

int main(){



int N;           //length of array
int all_even = 0;  // Intiailzing even and odd to false
int all_odd = 0;
printf("\nEnter the length of the array: ");   //asks user to input length
scanf("%d", &N);              

int array[N];    //sets length of array

printf("\nEnter the elements of the array: ");     // gets elements from user
for(int i=0; i<N; i++){
    scanf("%d", &array[i]);
}

find_parity(array,N,&all_even, &all_odd);   //calls the function with array, length, and addresses pointing to even and odd

if (all_odd == 1 && all_even ==0){                // using the new values of all_odd and all_even output is displayed to the user
    printf("\nOutput: good, all elements are odd");
}

else if(all_even == 1 && all_odd ==0){

    printf("\nOutput: good, all elements are even");

}

else 
    printf("\nOutput: not good");


}