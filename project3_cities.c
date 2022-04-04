#include <stdio.h>
#include <stdlib.h>  //This is for the exit function


/*

Adam Bricha (U9233-5585). This program accepts user input for number of cities, number of drones, and the list of drones.
Based off the user input that is validated, the program calculates 
how many cites be reached by atleast one drone.  This calcualtion is stored in an array and displayed to the user. This program uses nested for/while loops, if statements, 
and arrays.



*/
int main()
{

int N; // number of cities
int M; // number of drones
int location; // the current location of the drone
int distance; // Travel distance of each drone
int city1;  //cities vistited by the drone
int city2;
int city3;
int city4;
int city5;
int i;  // intialize variable for loop     
int Reached = 1;

printf("Enter number of cities: ");   //input for number of cities
scanf("%d",&N);
if (N <= 0 || N>=101){      //input validation
    printf("Invalid Input, Goodbye!");
    exit(0);   //exits the program
    
}
int CitiesReached[N]; //creates array with size of number of cities
    
printf("Enter number of drones: ");
scanf("%d",&M);
if(M <=0 || M>=101){       //input validation
    printf("Invlaid Input, Goodbye!");
    exit(0);     //exits the program
}
    
printf("Enter drone list:\n");  //user inputs ist of drones
for(i=0;i<M;i++)
{
    scanf("%d %d",&location,&distance);  
    city1 = location;       //sets location          
    city2 = location;
    CitiesReached[location] = 1;
    while(city1 > 0 && city2 <=N)
    {
        city2 = city2 + distance;
        city1 = city1 - distance;
        //based off the distance 
        if(city1 >0)
            CitiesReached[city1] = Reached;   //Marks the location as visited for city 1
        if(city2 <= N)
            CitiesReached[city2] = Reached;  //Marks the location as visted for city 2
        }
    }
    printf("Cities reached by a drone:\n");
    for(i=0;i<=N;i++)                      // displays the output to the user
    {
        if(CitiesReached[i] == Reached)  //if the city is reached print
            printf("%d ",i);
    }

}