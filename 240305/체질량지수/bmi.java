import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int height = sc.nextInt();
        int weight = sc.nextInt();
        
        // 키(cm)에서 키(m)로 단위 환산을 한 뒤 
	    // 체질량지수 계산 식에 넣어야 함에 유의
        int bmi = weight * 100 * 100 / ((height * height));
        System.out.println(bmi);

        if (bmi >= 25) {
            System.out.print("Obesity");
        }
    }
}