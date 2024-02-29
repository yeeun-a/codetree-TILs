public class Main {
    public static void main(String[] args) {
        // 1피트(ft)는 30.48cm이고 1마일(mi)은 160934cm
        float ft = 9.2f;
        float mi = 1.3f;

        System.out.printf("%.1fft = %.1fcm\n", ft, ft*30.48);
        System.out.printf("%.1fmi = %.1fcm", mi, mi*160934);
    }
}