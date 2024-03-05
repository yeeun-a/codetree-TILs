import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        char a = s.charAt(0);
        Double b = sc.nextDouble();
        Double c = sc.nextDouble();

        System.out.println(a);
        System.out.printf("%.2f\n%.2f", b, c);
    }
}