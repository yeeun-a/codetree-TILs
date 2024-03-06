import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        if (num == 1) {
            System.out.print("John");
        } else if (num == 2) {
            System.out.print("Tom");
        } else {
            System.out.print("Paul");
        }
    }
}