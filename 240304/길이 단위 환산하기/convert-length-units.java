import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Double ft1 = 30.48;

        Scanner sc = new Scanner(System.in);
        Double ft = sc.nextDouble();
        Double cm = ft * ft1;
        System.out.printf("%.1f", cm);
    }
}