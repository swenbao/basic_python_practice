#include<stdio.h>
#include<limits.h>

void printMatrix(int matrix[][6], int n) {
    int i, j;
    for(i = 1; i < n; i++) {
        for(j = 1; j < n; j++) {
            printf(" %d |", matrix[i][j]);
        }
        printf("\n-------------------------------------------------\n");
    }
    printf("\n///////////////////////////////////////////////\n");
}

int main(){
    int p[] = {2, 4, 3, 2, 5, 1};
    int n = sizeof(p)/4-1;

    int m[6][6]= {0};
    int s[6][6]= {0};
    for(int i = 1; i <= n; i++){
        m[i][i] = 0;
    }
    for(int l = 2; l <= n; l++){
        for(int i = 1; i <= n - l + 1; i++){
            int j = i + l - 1;
            m[i][j] = INT_MAX;
            for(int k = i; k <= j - 1; k++){
                int q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j];
                if(q < m[i][j]){
                    m[i][j] = q;
                    s[i][j] = k;
                }
            }

        }
    }

    printMatrix(m, 6);
    printMatrix(s, 6);


}