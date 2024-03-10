import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a_age = sc.nextInt();
        char a_sex = sc.next().charAt(0);
        int b_age = sc.nextInt();
        char b_sex = sc.next().charAt(0);

        if ((a_age >= 19 && a_sex == 'M') || (b_age >= 19 && b_sex == 'M'))
            System.out.print(1);
        else
            System.out.print(0);
    }
}