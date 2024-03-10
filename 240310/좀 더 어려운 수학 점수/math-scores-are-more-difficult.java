import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int aMath = sc.nextInt();
        int aEng = sc.nextInt();
        int bMath = sc.nextInt();
        int bEng = sc.nextInt();

        // if (aMath == bMath)
        //     System.out.print(aEng > bEng ? "A" : "B");
        // else if (aMath > bMath)
        //     System.out.print("A");
        // else
        //     System.out.print("B");

        if(a_math > b_math || (a_math == b_math && a_eng > b_eng))
            System.out.println("A");
        else
            System.out.println("B");
    }
}