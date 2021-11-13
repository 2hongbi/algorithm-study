package etc;

import java.util.Scanner;

public class Maze {
    static double EAST;
    static double WEST;
    static double NORTH;
    static double SOUTH;
    private static double[][] map;
    private static double VISITED;
    private static double NOT_VISITED;

    public static double visit(int x, int y, int count) {
        if (count == 0) {
            return 1.0;
        }
        count--;
        double ret = 0.0;
        map[x][y] = VISITED;

        if (map[x][y+1] == NOT_VISITED)
            ret += visit(x, y+1, count) * EAST;
        if (map[x][y-1] == NOT_VISITED)
            ret += visit(x, y-1, count) * WEST;
        if (map[x+1][y] == NOT_VISITED)
            ret += visit(x+1, y, count) * SOUTH;
        if (map[x-1][y] == NOT_VISITED)
            ret += visit(x-1, y, count) * NORTH;

        map[x][y] = NOT_VISITED;
        return ret;
    }

    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[i].length; j++) {
                map[i][j] = NOT_VISITED;
            }
        }

        int count = sc.nextInt();
        EAST = sc.nextInt()/100.0;
        WEST = sc.nextInt()/100.0;
        SOUTH = sc.nextInt()/100.0;
        NORTH = sc.nextInt()/100.0;

        System.out.println(visit(10, 10, count));
    }
}
