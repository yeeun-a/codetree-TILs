import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        if (a > b) {
            if (c > a)
                System.out.print(a);
            else if (c > b)
                System.out.print(c);
            else
                System.out.print(b);
        } else {
            if (c > b)
                System.out.print(b);
            else if (c > a)
                System.out.print(c);
            else
                System.out.print(a);
        }
    }
}