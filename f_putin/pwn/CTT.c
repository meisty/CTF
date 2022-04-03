#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>


int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  FILE *file;
  char flag[50];
  char secret_phrase[128];
  
  memset(flag, 0, sizeof(flag));
  memset(secret_phrase, 0, sizeof(secret_phrase));

  printf("What is Capture the Talent?\n");
  
  fgets(secret_phrase, sizeof(secret_phrase), stdin);
  char *end = strchr(secret_phrase, '\n');
  if (end != NULL) {
    *end = '\x00';
  }

  strcat(secret_phrase, ", good guess though");

  file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("You failed.");
    exit(0);
  }


  fgets(flag, sizeof(flag), file);

  printf("Hmmmmm.....not sure where you heard that. Definitely not via @ssh4un, @amysw_sec or @capturetalent ");
  puts(secret_phrase);

  return 0;
}
