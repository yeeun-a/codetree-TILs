public class Main {
    public static void main(String[] args) {
        int a = 5, b = 6, c = 7;
        a = b = c; // c의 값을 a, b에 복사
        System.out.printf("%d %d %d", a, b, c);
    }
}