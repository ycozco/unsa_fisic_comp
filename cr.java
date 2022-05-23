import java.util.*;

public class cr {
    public static void main(String[] args) {
        System.out.println("ingrese el valor ");
        Scanner sc = new Scanner(System.in);
        int value = sc.nextInt();
        String result = perfect_square_recursive(1, value);
        System.out.println(result);
    }

    static int perfect_square(int number) {
        int result = 0;
        for (int i = 1; i <= number; i++) {
            if (i * i == number) {
                result = i;
                break;
            }
        }
        return result;
    }

    static String perfect_square_recursive(int test, int number) {
        if (test * test == number) {
            return test + "";
        } else if (test * test > number) {
            return "No es cuadrado perfecto";
        } else {
            return perfect_square_recursive(test + 1, number);
        }
    }
}