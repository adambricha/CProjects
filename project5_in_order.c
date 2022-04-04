#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/* Adam Bricha (U9233-5585). This program accepts user input checks to see if the character(s) is in order or not. For a character to be in order it must follow
these three conditions:
1. are alphabetic letters, lower case or upper case.  
2. any two neighboring letters (regardless of case) are in order
3. if two neighboring letters are same, they are considered in order.  
 
This program uses command line arguements

*/





int in_order(char *word){
    
    int inorder = 1; // in order
    int len = strlen(word);
    
    for(int i= 0; i< len; i++){     // makes lowercase
        word[i]= tolower(word[i]);
    }
    for(int j=0;j<len-1;j++){       //checks to see alphabetic letters
        if(word[j]<'a' || word[j]>'z'){   
            inorder = 0; //not in order
            break;
        }
         if(word[j]>word[j+1]){   /// checks to see neighboring letters
            inorder = 0;   // not in order
            break;  
    }
    }

if(inorder){
    printf("\nOutput: In order");
    }
else{
    printf("\nOutput: Not in order");
    }
}



int main(int argc, char* argv[])
{
    int inorder;
    if(argc!=2){                                         //input validation
        printf("Output: Incorrect number of arguments");
        exit(0);
    }
    
    else
        in_order(argv[1]);     //calls the function to check if in order
}



