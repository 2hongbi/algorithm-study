package etc;

import java.math.BigInteger;
import java.util.Arrays;
import java.util.Random;

public class Q1Sort {
    public static void main(String[] args) {
        int n = 2000;
        int []numbers = new int[n];
        int rand_seed = 914;
        Random r = new Random(rand_seed);

        BigInteger max = BigInteger.valueOf(1);

        for (int i = 0; i < n; i++) {
            numbers[i] = r.nextInt(999) + 1;
        }
        Arrays.sort(numbers);

        numbers[0]++;
        for (int i = 0; i < n; i++) {
            max = max.multiply(BigInteger.valueOf(numbers[i]));
        }
        System.out.println(max);
    }
}
