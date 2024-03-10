import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char a_sym = sc.next().charAt(0);
        int a_temp = sc.nextInt();
        char b_sym = sc.next().charAt(0);
        int b_temp = sc.nextInt();
        char c_sym = sc.next().charAt(0);
        int c_temp = sc.nextInt();

        if (a_sym == 'Y' && a_temp >= 37) {
            if ((b_sym == 'Y' && b_temp >= 37)|| (c_sym == 'Y' && c_temp >= 37))
                System.out.print('E');
            else
                System.out.print('N');
        } else {
            if ((b_sym == 'Y' && b_temp >= 37) && (c_sym == 'Y' && c_temp >= 37))
                System.out.print('E');
            else
                System.out.print('N');
        }
    }
}