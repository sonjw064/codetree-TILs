import java.util.Scanner;

public class Main {
    public static int n, m;
    public static int[] a = new int[101];

    public static int check() {
        int sum = 0;

        while (m >= 1) {
            sum += a[m - 1];

            if (m == 1) {
                break;
            }

            if(m % 2 == 0){
                m = m / 2;
            }
            else {
                m = m - 1;
            }
        }
        return sum;
    }
    public static void main(String[] args) {
        Scanner sc =  new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();

        for (int i = 0; i < n; i++){
            a[i] = sc.nextInt();
        }
        System.out.println(check());
        
    }
}