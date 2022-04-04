#include <stdio.h>

/* Adam Bricha (U9233-5585). This program accepts a list of numbers and calculates the factorial of these numbers. The first array stores the inputed values 
and the secound array stores the calculate values. This program uses arrays, functions and recursion.
*/


//declaring functions that will be defined and used later in the program
int fact(int length);     
void calculate_fact(int array1[],int length,int array2[]);
int main()
{
    
int length;

printf("Enter the length of the array: ");   //accepts user input for length of the array(how many numbers they will be calculating the factorial of)
scanf("%d",&length);
int array1[length]; //array for calculating 
int array2[length]; //array for storing calculated numbers
    

printf("Enter the elements of the array: ");    //stores elements that the user entered
for(int i=0;i<length;i++){
    printf("\na[%d]:",i);
    scanf("%d",&array1[i]);
}   
calculate_fact(array1,length,array2);  //uses the function to calculate the factorial
   
printf("Output: ");        
for(int j=0;j<length;j++){    // printing the stored outputs of the array 2(the factorial)
    printf("%d ",array2[j]);
}

}

int factofzero = 1; //special case for factorial of zero 1

int fact(int length) {            
    if (length == 0) {    //Factorial of 0 is 1
        return factofzero;
    }
    else if (length >0){     // if the user enters any other number than zero
        return length * fact(length-1);
        }  
}

//defines the fucntion for calculating the factorial and storing the values
void calculate_fact(int array1[],int length,int array2[]){
    for(int k=0;k<length;k++){ 
        int temp;
        temp = fact(array1[k]); //go through the values of A, calculate the factorial, and swap them into the secound array
        array2[k]=temp;
    }
}