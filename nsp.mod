/*********************************************
 * OPL 22.1.1.0 Model
 * Author: Laptop
 * Creation Date: 10 maj 2023 at 17:06:13
 *********************************************/
int M = 10; //liczba pielęgniarek
int P = 7; // liczba dni tygodnia
int k = 24; // do tego maja sie sumowac godziny na zmianie po wszystkich pielegniarkach
int p[1..P, 1..M] = [[10, 5, 10, 7, 9, 11, 11, 11, 6, 8],
					[6, 11, 12, 5, 10, 9, 12, 6, 8, 10],
					[9, 8, 8, 11, 5, 11, 12, 5, 11, 6],
					[7, 5, 8, 5, 11, 12, 5, 5, 11, 10],
					[10, 6, 6, 11, 7, 12, 10, 11, 5, 9],
					[7, 12, 10, 6, 10, 11, 7, 9, 10, 6],
					[5, 5, 6, 5, 9, 10, 6, 8, 8, 11]
					
]; //dyspozycja podana przez pielęgniarki
int c[1..M] = [39,43,42,51,38, 50, 37, 40, 38,49]; //stawka godzinowa każdej pielegniarki
dvar boolean x[1..P, 1..M]; //zmienna decyzyjna
minimize sum(i in 1..P) sum(j in 1..M) p[i,j]*x[i,j]*c[j]; //minimalizacja sumy przepracowanych godzin dla każdej pielegniarki z uwzglednieniem kosztów jej zatrudnienia
subject to {
             forall(i in 1..P){
                sum(j in 1..M)(p[i][j])*x[i][j] == k;
             };
             forall(j in 1..M){
                sum(i in 1..P)(p[i][j])*x[i][j] <= w;
        };
             //forall(j in 1..M){
              //  sum(i in 1..P)(p[i][j])*c[j]*x[i][j] == q;
      //  };
            forall(j in 1..M){
                1 <= sum(i in 1..P) x[i][j];
            };   }
