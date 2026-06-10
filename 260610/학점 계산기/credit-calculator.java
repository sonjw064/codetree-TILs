import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        double sum = 0;
        int cnt = 0;
        double avl = 0;
        double arr[] = new double[n];
        for (int i = 0; i < n; i++){
            arr[i] = sc.nextDouble();
        }
        for (int i = 0; i < n; i++){
            sum += arr[i];
            cnt += 1;
        }
        avl = sum / cnt;
        System.out.printf("%.1f\n",avl);
        if (avl >= 4.0){
            System.out.print("Perfect");
        }
        else if (avl >= 3.0){
            System.out.print("Good");
        }
        else {
            System.out.print("Poor");
        }
    }
}