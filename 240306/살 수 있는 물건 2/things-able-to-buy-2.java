import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int budget = sc.nextInt();

        if (budget >= 3000) {
            System.out.print("book");
        } else if (budget >= 1000) {
            System.out.print("mask");
        } else if (budget >= 500) {
            System.out.print("pen");
        } else {
            System.out.print("no");
        }
    }
}