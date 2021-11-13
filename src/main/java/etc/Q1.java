package etc;

import java.math.BigInteger;
import java.util.Random;

public class Q1 {
    public static void main(String[] args) throws Exception{
        int n = 2000;
        int []numbers = new int[n];
        int rand_seed = 914;
        Random r = new Random(rand_seed);

        BigInteger[] results = new BigInteger[n];
        BigInteger max;

        for (int i = 0; i < n; i++) {
            results[i] = BigInteger.valueOf(1);
        }

        for (int i = 0; i < n; i++) {
            numbers[i] = r.nextInt(999) + 1;
        }

        for (int i = 0; i < n; i++) {
            numbers[i]++;
            for (int j = 0; j < n; j++) {
                results[i] = results[i].multiply(BigInteger.valueOf(numbers[j]));
            }
            numbers[i]--;
        }

        max = results[0];
        for (int i = 1; i < n; i++) {
            if (max.compareTo(results[i])==1)
                max = results[i];
        }
        System.out.println(max);
        System.out.println(results);
    }
}
