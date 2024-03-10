import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int a_math = sc.nextInt();
        int a_eng = sc.nextInt();
        int b_math = sc.nextInt();
        int b_eng = sc.nextInt();

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