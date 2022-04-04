#include <stdio.h>
#include <string.h>

// Adam Bricha (U9233-5585) This program reads in files from the command line arguement and concatanates each line as long as the amount of letters is less than M.
// This program uses a function with a file pointer to read everything in the file, integer max length and prints the values that become concatenated intp the array



void computesuffix(FILE *file, int M);   // This function takes in the file pointer, M, and prints concatanated string



int main(int argc , char *argv[]) {            //argc = how many files, argv = name of files

        int M;
        printf("Enter the value of M = ");         
        scanf("%d", &M);  
        
for(int i=1; i<argc; i++) {                   // dont include ./a.out, i starts at 1 and reads the files
        printf("%s : ", argv[i]);                
        computesuffix((fopen(argv[i], "r")), M);             
        printf("\n");
        }
        
}




void computesuffix(FILE *file, int M) {        
        
        int length;
        char output[100] = "";             // each file starts with empty string    
        char input[21];                      
        
while(fgets(input, 21, file) != NULL) {          
        if(strlen(input)-1 > M)                   
                continue;                         
        
        else if(strlen(input)-1 > M-length) {         
                strcpy(output, "");                  //empty the array
                }
                
                
        strncat(output, input, strlen(input)-1);       //concatanate the input file onto the suffix file (N numbers)
        length = strlen(output);                      //new length

        }

        printf("%s", output);         
        fclose(file);       

}