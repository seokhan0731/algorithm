import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static final int numberOfColor = 3;

    static void getEachMinimumCase(int[] color, int[] temp) {
        color[0] = Math.min(temp[1], temp[2]);
        color[1] = Math.min(temp[0], temp[2]);
        color[2] = Math.min(temp[0], temp[1]);
    }

    public static void main(String[] args) throws IOException {
//        System.setIn(new FileInputStream("input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        //R:0 G:1 B:2
        int[] color = new int[numberOfColor];
        int[] temp = new int[numberOfColor];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            if (i == 0) {
                for (int k = 0; k < numberOfColor; k++) {
                    color[k] = Integer.parseInt(st.nextToken());
                }
                continue;
            }

            temp = Arrays.copyOf(color, color.length);
            getEachMinimumCase(color, temp);

            for (int k = 0; k < numberOfColor; k++) {
                color[k] += Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(Arrays.stream(color).min().getAsInt());
    }
}