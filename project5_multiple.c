#include <stdio.h>
#include <string.h>

// Adam Bricha(U9233-5585) This program accepts user input for a number then checks if it is a multiple of 11 or not.
// The program checks if the difference of the sum of the digits at odd places and even places of X is 0 or a multiple of 11, then X is a multiple of 11 as well.



int multiple_of_11(char *ch,int N){

int multiple = 0; // sets multiple to false
for (int j = 0; j < N; ++j) //go through each digit in the array
{
        if(j % 2 == 0) 
                multiple +=(ch[j] - '0'); 
        else if(j % 2 != 0)
                multiple -= (ch[j] - '0');
        }

return multiple % 11 == 0;

}
int main()
{

char array_of_digits[1000];  //sets array of digits with length 1000
              
printf("Enter the value of X: "); //asks user to input value for x
int i = 0; // sets value of i to zero

while((array_of_digits[i++] = getchar())!= '\n');   //as long as the user doesnt hit enter keep reading values
        array_of_digits[--i] = 0; 
        
        
if(multiple_of_11(array_of_digits,i))                       // print result to the user
        printf("%s is a multiple of 11",array_of_digits);
else 
        printf("%s is not a multiple of 11",array_of_digits);

}