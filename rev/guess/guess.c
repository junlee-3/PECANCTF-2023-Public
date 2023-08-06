#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

int main()
{
  srand(time(NULL));
  // Dummy flag
  char *fakeFlag = "PECAN{THIS_IS_NOT_THE_FL@G}";

  printf("Welcome to George's guessing game.\n");
  printf("If you guess the number right I will tell you the secret flag.\n\n");

  char flag[27] = {0};

  // The correct number
  int correct = rand() % 100 + 1;
  // int correct = 50;
  while (true)
  {
    printf("Guess a number between 0 and 100:\n");

    // Get a number from stdin
    // This goes into an infinite loop if a non number is printed
    //  - This is a feature not a bug
    int number;
    scanf("%d", &number);

    if (number == correct)
    {
      // Fill out flag
      // flag[0] is set to 0 intentionally to stop the printing code.
      flag[1] = 'p';
      flag[2] = 'e';
      flag[3] = 'c';
      flag[4] = 'a';
      flag[5] = 'n';
      flag[6] = '{';
      flag[7] = 'H';
      flag[8] = '0';
      flag[9] = 'W';
      flag[10] = '-';
      flag[11] = 'd';
      flag[12] = '0';
      flag[13] = '-';
      flag[14] = '1';
      flag[15] = '-';
      flag[16] = 'P';
      flag[17] = 'R';
      flag[18] = '1';
      flag[19] = 'n';
      flag[20] = 't';
      flag[21] = '-';
      flag[22] = '7';
      flag[23] = 'h';
      flag[24] = 'i';
      flag[25] = 'S';
      flag[26] = '}';

      printf("Correct, the flag is: %s\n", flag);
      return 0;
    }
    else if (number < correct)
    {
      printf("Higher:\n");
    }
    else
    {
      printf("Lower:\n");
    }
  }
}
