#include<stdio.h>
#include <limits.h>
#include <float.h>

int main(){
    int n = 7;

    double p[] = {-1, 0.05, 0.1, 0.15, 0.1, 0.2, 0.3, 0.1};
    double e[9][8] = {0};
    int root[8][8] = {0};
    double w[9][8] = {0};

    for(int i = 1; i <= n+1; i++){
        e[i][i-1] = 0;
        w[i][i-1] = 0;
    }

    for(int l = 1; l <= n; l++){
        for(int i = 1; i <= n - l + 1; i++){
            int j = i + l - 1;
            e[i][j] = DBL_MAX;
            w[i][j] = w[i][j-1]+p[j];
            for(int r = i; r <= j; r++){
                double t = e[i][r-1] + e[r+1][j] + w[i][j];
                if(t < e[i][j]){
                    e[i][j] = t;
                    root[i][j] = r;
                }
            }
        }
    }
    //-----------------------
    printf("Array e:\n");
    for (int i = 1; i <= n+1; i++) {
        for (int j = 0; j <= n; j++) {
            printf(" %.2f |", e[i][j]);
        }
        printf("\n-------------------------------------------------------\n");
    }

    printf("\nArray root:\n");
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            printf(" %d |", root[i][j]);
        }
        printf("\n----------------------------------\n");
    }

    printf("\nArray w:\n");
    for (int i = 1; i <= n+1; i++) {
        for (int j = 0; j <= n; j++) {
            printf(" %.2f |", w[i][j]);
        }
        printf("\n-----------------------------------------------------\n");
    }

    return 0;
}