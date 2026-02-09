#include <stdio.h>
#include <stdlib.h>

typedef enum
{
   ADD,
   MULT,
   SUBTRACT,
   DIV,
   UNSUPPORTED
} MathOperation;

void IssueBadNumberError()
{
    printf("The string does not represent a floating point number.\n");
    exit(EXIT_FAILURE);
}
void IssueBadOperationError()
{
    printf("The string does not represent a valid operation.\n");
    exit(EXIT_FAILURE);
}

MathOperation GetOperation(char *op)
{
    /* Implement me! */
    char my_operation = *op;    /*variable to hold the operator char*/
    char *next_char = op + 1;   /*pointer to the next char*/
    if (*next_char != '\0') {   /*if the char following my_operation isn't null, operation is invalid, so exit*/
        exit(2);
    }
    switch (my_operation) {
        case '+':
            return ADD;
        case '-':
            return SUBTRACT;
        case 'x':
            return MULT;
        case '/':
            return DIV;
        default:
            exit(2);
    }
    return 0;
}


double StringToDouble(char *str)
{
    /*declare variables*/
    char *curr_num = str;       /*variable that stores value of pointer str*/              
    double my_double = 0.;       /*double that will hold final result*/
    int current_num;            /*integer version of curr_num, to add to double*/
    char sign = '+';                  /*holds the sign of number*/
    int is_fraction = 0;            /*0 = not fraction and 1 = is fraction*/
    double before_decimal = 0.;     /*variable to store part before decimal*/
    double after_decimal = 0.;      /*variable to store part after decimal*/
    
    /*check if the number is positive or negative*/
    if (*curr_num == '-') {     /*sees if the first character is a negative sign*/
        sign = '-';             /*sets sign var to hold the negative sign*/
        *curr_num++;
    }

    /*create the part of the double before the decimal*/
    while (*curr_num != '\0' && is_fraction == 0) {
        if (*curr_num == '.') {             /*if its the decimal, switch to building the fraction component*/
            is_fraction = 1;
            *curr_num++;
            break;
        }
        else if (!(*curr_num >= 48 && *curr_num <= 57)) {       /*exit if value isn't a digit*/
            exit(2);
        }
        current_num = *curr_num - 48;                           /*convert ASCII value to integer value*/
        before_decimal = (before_decimal * 10) + current_num;   /*move numbers over, add integer so it is in the right position*/
        *curr_num++;
        }
        

    /*create the part of the double after the decimal*/
    double dec_place = 0.1;         /*variable to track how many places to move after_decimal over*/
    while (*curr_num != '\0' && is_fraction == 1) {
        if (!(*curr_num >= 48 && *curr_num <= 57)) {        /*exit if *curr_num isn't a digit value*/
            exit(2);
        }
        current_num = *curr_num - 48;                       /*convert ASCII to integer digit*/
        double frac_value = current_num * dec_place;        /*move number to correct decimal place*/
        after_decimal = after_decimal + frac_value;
        *curr_num++;
        dec_place = dec_place * 0.1;                        /*move decimal place back by one*/
    }

    /*add before and after decimal parts together*/
    my_double = before_decimal + after_decimal;

    /*fix the sign of the double*/
    if (sign == '-') {
        my_double = my_double * -1;
    }

    return my_double;
}


int main(int argc, char *argv[])
{
    double v = StringToDouble(argv[1]);
    MathOperation op = GetOperation(argv[2]);
    double v2 = StringToDouble(argv[3]);
    double result = 0.;
    switch (op)
    {
        case ADD:
            result = v + v2;
            break;
        case SUBTRACT:
            result = v - v2;
            break;
        case MULT:
            result = v * v2;
            break;
        case DIV:
            result = v / v2;
            break; 
    }
    printf("%d\n", (int) result);
 
    return 0;
}
