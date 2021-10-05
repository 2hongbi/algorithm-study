package practice.ch01;

import java.util.Scanner;

public class Max4 {
    static int max4(int a, int b, int c, int d) {
        // 네 값의 최댓값을 구하는 메서드
        int max = a;
        if (b > max)
            max = b;
        if (c > max)
            max = c;
        if (d > max)
            max = d;
        return max;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b, c, d;

        System.out.println("--네 정수의 최댓값 구하기--");
        System.out.print("a의 값 : ");
        a = sc.nextInt();
        System.out.print("b의 값 : ");
        b = sc.nextInt();
        System.out.print("c의 값 : ");
        c = sc.nextInt();
        System.out.print("d의 값 : ");
        d = sc.nextInt();

        int max = max4(a, b, c, d);
        System.out.printf("최대값은 %d 입니다.", max);
    }
}
