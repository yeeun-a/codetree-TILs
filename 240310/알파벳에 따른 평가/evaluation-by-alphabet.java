import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();

        if (s.charAt(0) == 'S') {
            System.out.print("Superior");
        } else if (s.charAt(0) == 'A') {
            System.out.print("Excellent");
        } else if (s.charAt(0) == 'B') {
            System.out.print("Good");
        } else if (s.charAt(0) == 'C') {
            System.out.print("Usually");
        } else if (s.charAt(0) == 'D') {
            System.out.print("Effort");
        } else {
            System.out.print("Failure");
        }
    }
}