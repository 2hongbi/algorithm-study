package etc;

import java.util.Scanner;

public class ClockSync {

    public static int INF = 9999, SWITCH = 10, CLOCK = 16;

    static int[] clocks = new int[CLOCK];

    public static int[][] switches = {
            {0, 1, 2},
            {3, 7, 9, 11},
            {4, 10, 14, 15},
            {0, 4, 5, 6, 7},
            {6, 7, 8, 10, 12},
            {0, 2, 14, 15},
            {3, 14, 15},
            {4, 5, 7, 14, 15},
            {1, 2, 3, 4, 5},
            {3, 4, 5, 9, 13}
    };

   private static boolean checkTwelve() {
        // 모든 시계가 12시를 가르키는지 확인, 하나라도 12시 아니면 false
        for(int i = 0; i < CLOCK; i++) {
            if (clocks[i] % 4 != 0)
                // if (clocks[i] != 12)
                return false;
        }
        return true;
   }


   public static void pressButton(int number) {
       // switch 누름
        for (int i = 0;i < switches[number].length;i++) {
            int time = switches[number][i];
            clocks[time] += 3; // 누를 때 마다 3시간만큼 움직임
            if(clocks[time] == 15) {
                clocks[time] = 3;
            }
        }
   }

   public static int solve(int number) {
        if (number == SWITCH) {
            return checkTwelve() ? 0 : INF;
        }
        int ret = INF;
        for (int cnt = 0; cnt < 4; cnt++) { // 스위치 0~3번 눌러보기
            ret = Math.min(ret, cnt + solve(number + 1)); // 작은 값 저장
            pressButton(number);
        }
        return ret;
   }

   public static void main(String[] args) {
        Scanner  sc = new Scanner(System.in);
        int c = sc.nextInt();

        for (int i = 0; i < c; i++) {
            for (int j = 0; j < CLOCK; j++) {
                clocks[j] = sc.nextInt();
            }

            int answer = solve(0);
            System.out.println(answer == INF ? -1 : answer);
        }
        sc.close();
   }

}
