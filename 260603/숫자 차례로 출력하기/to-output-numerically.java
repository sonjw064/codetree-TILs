import java.util.Scanner;

public class Main {
    public static void star(int n){
        if (n == 0){
            return;
        }
        
        star(n-1);
        System.out.print(n + " ");
        }
    
    public static void restar(int n){
        if (n == 0){
            return;
        }
        System.out.print(n + " ");
        restar(n-1);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        star(n);
        System.out.println("");
        restar(n);
    }
}