#include <stdio.h>

/*



Adam Bricha (U9233-5585)

This program accepts input from the user to determine when Comet Halley will next be seen. The user enters in the current year and

the program will display when the next time Comet Halley will appear.



*/



int main(){



int year; // declares variable for year
int nextapp;
int years_passed;
int difference;
printf("\nEnter Year: "); // accpets user input for year

scanf("%d", &year);



if (year >= 1986){
    years_passed = (year-1986) % 76;
    difference = 76-years_passed;  //calculates next time comet will be seen based off user input
    nextapp = year + difference;




    printf("Next Apperance: %d", nextapp);


}
else{

 printf("That is not a valid date");

}
}