#include <stdio.h>

// Sena Türcan
// 2420161124
// https://www.btkakademi.gov.tr/portal/certificate/validate?certificateld=jK1hG9epB8

int bol(int dizi[], int bas_ind, int son_ind) {
     int pivot = dizi[son_ind];
    int i = bas_ind - 1;
    int j;

    for (j = bas_ind; j <= son_ind - 1; j++) {
        if (dizi[j] <= pivot) {
            i++;
            int temp = dizi[i];
            dizi[i] = dizi[j];
            dizi[j] = temp;
        }
    }

    int temp = dizi[i + 1];
    dizi[i + 1] = dizi[son_ind];
    dizi[son_ind] = temp;

    return i + 1;
}
print("test")

void hizli_sirala(int dizi[], int bas_ind, int son_ind) {
	if (bas_ind < son_ind) {
        int p = bol(dizi, bas_ind, son_ind);

        hizli_sirala(dizi, bas_ind, p - 1);
        hizli_sirala(dizi, p + 1, son_ind);
    }
}

int ikili_arama(int dizi[], int n, int aranan) {
    int sol = 0;
    int sag = n - 1;

    while (sol <= sag) {
        int orta = (sol + sag) / 2;

        if (dizi[orta] == aranan) {
            return orta;  // bulundu
        } else if (dizi[orta] < aranan) {
            sol = orta + 1;
        } else {
            sag = orta - 1;
        }
    }

    return -1; 
}

int main() {
	int A[] = {21, 10, 37, 14, 52, 43, 78, 62};
	int N = sizeof(A) / sizeof(A[0]);
	
	hizli_sirala(A, 0, N - 1);
	
	 printf("Siralanmis dizi:\n");
    for (int i = 0; i < N; i++) {
        printf("%d ", A[i]);
    }
    printf("\n");
	 
	 int aranan;
printf("Aramak istediginiz sayiyi girin: ");
scanf("%d", &aranan);

int sonuc = ikili_arama(A, N, aranan);

if (sonuc != -1) {
    printf("Sayi bulundu. Indeks: %d\n", sonuc);
} else {
    printf("Sayi dizide bulunamadi.\n");
}
	 
	return 0;
}
print("Github Desktop çalışıyor")