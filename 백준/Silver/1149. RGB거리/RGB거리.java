import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 기존 코드. 바텀업 방식의 dp 사용
 * dp는 결국 점화식을 뽑아내는게 우선이기에, n일 때의 어떠한 값들이 들어올 수 있는지에 대해 초기에 집중함
 * 결국 문제 조건에서, n번째에는 n-1번째에 들어오지 않은 색만이 들어올 수 있다는 규칙만 지키면, 문제 조건에
 * 위배되는 케이스가 없다고 판단함.
 * 이에 따라 초기에는 단순히 d[n]=d[n-1]+min(n) 정도로 생각을 했지만,
 * 이 점화식이 n+1번째에 어떤 값이 들어오냐에 따른 최소값을 보장할 수 없다는 것을 깨달았다.
 *
 * => 결국 해당 문제에서는 세 가지 상태를 다 봐주어야 한다. n-1번째에서 R, G, B로 오는 경우의 최소값을
 * dp 기법을 통해 저장한 상태로, dp의 점화식 토대를 사용하여, 계속 갱신해주는 로직을 짜야 했다.
 *
 * +) 해당 과정에서 결국 직전의 3가지 상태에 대한 비용값만 필요하기 때문에, 굳이 dp테이블을 만들지 않고,
 * temp[]를 통해, 메모리를 아끼고자 하였다. 이에 따라, 해당 로직은 매 루프마다
 * 기존 비용 temp[]로 복사->최소값 계산->갱신->루프 종료 순으로 이루어진다.
 *
 *      +)처음에 점화식을 짠 직 후, 각 케이스별로 보는 것이
 *        브루트포스 알고리즘 성격이 강하다고 생각하여, 아닐 것이라 생각했지만, 브루트포스는 모든 상태를 다 접근해보지만,
 *        dp는 n-1번째까지에서 최소값이 되는 케이스만 보고 저장하기 때문에, 살짝 성격이 다르다는 점을 파악했다.
 *        (사실 개인적인 생각으로는 브루트포스적 성격이 섞여있는 문제라고 생각이 들었다.)
 */
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

        st = new StringTokenizer(br.readLine());
        for (int k = 0; k < numberOfColor; k++) {
            color[k] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            System.arraycopy(color, 0, temp, 0, color.length);
            getEachMinimumCase(color, temp);

            for (int k = 0; k < numberOfColor; k++) {
                color[k] += Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(Arrays.stream(color).min().getAsInt());
    }
}
