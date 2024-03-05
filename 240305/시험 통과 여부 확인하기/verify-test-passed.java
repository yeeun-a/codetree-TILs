import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int more = 80 - a;

        if (a >= 80) {
            System.out.print("pass");
        } else {
            System.out.printf("%d more score", more);
        }
    }
}