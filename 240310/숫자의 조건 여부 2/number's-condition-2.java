import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();

        if (a == 5) {
            System.out.print("A");
        }

        if ((a%3) == 0) {
            System.out.print("B");
        }
    }
}