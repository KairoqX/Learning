#include <stdio.h>
#include<stdbool.h> // use for boolean

int main(){
    int age = 17; //intiger or whole numbers 4 bytes
    int year = 2026;
    float gpa = 2.5; //floating point they can only store 6 to 7 digit after decimal 4 b
    double pi = 3.14556589754645; // double can store arround 15 digit after decimal
    char grade = 'A'; // char only stores on character
    char symbol = '@'; // also dont use "" for chars use ''
    char name[] = "KairoqX"; // to store more that on character we use arry with the var name and [] ot becomes string use "" for string
    bool isOnline = true; //bool only stores true or false true is 1 and false is 0

    printf("You are %d years old\n", age); //%d for decimals
    printf("The year is %d\n", year);

    printf("Your gpa is %.1f\n", gpa); // %f for float .1 shows only 1 digit after the decimal
    
    printf("Pi is %lf\n", pi); //%lf means long float it use for double c displays 6 digits after decimal so use . and the no of digits you want like %.15lf

    printf("your grade is %c\n", grade); // %c use for char 

    printf("Your name is %s\n", name); // %s use for strings 
    
    printf("%d\n", isOnline); // it will return 0 or 1 

    if(isOnline){
        printf("you are online");
    }
    else{
        printf("You are offline");
    }
    return 0;
}