public class Main {
    public static void main(String[] args) {
        int a = 5, b = 6, c = 7;
        int temp = a, temp2 = b; //7
        a = c; // 7
        b = temp; // 5
        c = temp2; // 6
        System.out.printf("%d\n%d\n%d", a, b, c);
    }
}