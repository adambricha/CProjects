// Adam Bricha(U9233-5585)
// This program reads a CSV document of states in the US. With the information in the CSV it sorts the states by population over 65 and writes it
// to another file. The user can decide which file to open and to write to. This program uses functions, structures, and file input/output


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct state{               //each states has these elements
    char name[200];
    int pop2020;
    int pop2010;
    double popunder5;
    double popunder18;
    double popover65;


};

void sort_states(struct state list[], int n);  //function to store states by popluation over age 65. Takes in list of states and number of states

int main(){
 

    struct state states[101];    // list of structure states
    char filename[150];
    char outputfile[150] = "sorted_";


    printf("Enter the name of the file:  ");
    scanf("%s", filename);

    FILE *p;
    p = fopen(filename, "r");

    FILE *q;
    q = fopen(outputfile, "w");

    strcat(outputfile, filename);

    if(p == NULL){                  // if input file doesn't exists
        printf("file not found");
        exit(0);

    }
   
    int n= 0; // number of states starting at index 0


    while(!feof(p)  && !ferror(p))    //reading the file 
    {           
        fscanf(p, "\n%[^,], %d, %d, %lf, %lf, %lf",states[n].name,&states[n].pop2020,&states[n].pop2010,&states[n].popunder5,&states[n].popunder18,&states[n].popover65);
        n++;            
    }
        sort_states(states, n);    //calls sort states with list of states and number of states
        
        printf("\nOutput file name:\n%s\n", outputfile);
        printf("\n");


    for(int i =0; i<n-1; i++){      //write to output

        fprintf(q, "%s, %d, %d, %.1lf, %.1lf, %.1lf\n",states[i].name,states[i].pop2020,states[i].pop2010,states[i].popunder5,states[i].popunder18,states[i].popover65);
  
    } 

    fclose(p);    //close the files
    fclose(q);

}


void sort_states(struct state list[], int n){         //sort by population by age over 65
    for(int i =0; i <n; i++){
        for(int j=0; j<n-1; j++){                               //bubble sort
            if (list[i].popover65 > list[i+1].popover65){
                struct state temp = list[j];
                list[j] = list[j+1];
                list[j+1] =temp;
                
            }
        }
    }

}
