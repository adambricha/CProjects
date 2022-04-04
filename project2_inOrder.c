#include <stdio.h>
#include <ctype.h>
/* Adam Bricha (U9233-5585). This program accepts user input checks to see if the character(s) is in order or not. For a character to be in order it must follow
these three conditions:
1. are alphabetic letters, lower case or upper case.  
2. any two neighboring letters (regardless of case) are in order
3. if two neighboring letters are same, they are considered in order.  
 



*/

int main(){
    char c[26]; ///accepts character input from the yser
    int numofletters = 0; 
    int i; 
    int inorder = 1; //setting boolean to TRUE
    printf("Input: ");
    
    char firstletter; 
    firstletter = getchar();  //reads the first letter that the user input
    
    while(firstletter !='\n'){ ///converts the characters into a string
        c[numofletters] = firstletter;
        numofletters++; 
        firstletter = getchar(); 
    }
  for(int index = 0; c[index]; index++){ //Makes the string lowercase
  c[index] = tolower(c[index]);
}


    for(i=0;i<numofletters-1;i++){       //checks to see if the characters is in order
        if(c[i]<'a' || c[i]>'z'){   //if its not in the alaphabet
            inorder = 0; //FALSE(Not in order)
            break; //ends the loop
        }
        if(c[i]>c[i+1]){   /// checks to see neighboring letters
            inorder = 0; // FALSE(not in order)
            break; // ends the loop 
        }
    }
    
    if(inorder){
        printf("\nOutput: In order");
    }
    else{
        printf("\nOutput: Not in order");
    }
}