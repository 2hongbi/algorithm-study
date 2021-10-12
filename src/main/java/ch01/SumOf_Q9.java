package ch01;

import java.util.Scanner;

public class SumOf_Q9 {
    static int sumof(int a, int b) {
        if (b < a) {
            int temp = b;
            b = a;
            a = temp;
        }
        int sum = 0;
        for (int i = a; i <= b; i++) {
            sum += i;
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("a와 b를 포함하여 그 사이의 모든 정수의 합을 구합니다.");
        System.out.print("a의 값：");
        int a = sc.nextInt();
        System.out.print("b의 값：");
        int b = sc.nextInt();

        System.out.println("정수 a, b 사이의 모든 정수의 합은 " + sumof(a, b) + "입니다.");

        
    }
}
