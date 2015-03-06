#include <stdio.h>

int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    char line[1024];
    while (fgets(line, 1024, file)) {
        for(int i = 0; line[i]; i++) {
            line[i] = tolower(line[i]);
        }
        printf(line);
    }
}
