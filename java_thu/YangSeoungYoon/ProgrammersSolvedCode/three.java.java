3.
import java.util.*;

public class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        // 각 작업의 남은 일수를 저장할 리스트
        List<Integer> days = new ArrayList<>();
        
        // 남은 일수를 계산하여 리스트에 추가
        for (int i = 0; i < progresses.length; i++) {
            int remainingProgress = 100 - progresses[i];
            int remainingDays = (int) Math.ceil((double) remainingProgress / speeds[i]);
            days.add(remainingDays);
        }
        
        // 결과를 저장할 리스트
        List<Integer> result = new ArrayList<>();
        
        // 첫 번째 배포일을 기준으로 설정
        int firstDeployDay = days.get(0);
        int count = 1;
        
        // 두 번째 작업부터 순회하면서 배포일을 결정
        for (int i = 1; i < days.size(); i++) {
            if (days.get(i) <= firstDeployDay) {
                // 현재 작업이 첫 번째 배포일에 포함될 수 있는 경우
                count++;
            } else {
                // 새로운 배포가 필요한 경우
                result.add(count);
                firstDeployDay = days.get(i);
                count = 1;
            }
        }
        
        // 마지막으로 남은 작업들에 대한 배포
        result.add(count);
        
        
        
        // 결과를 배열로 변환하여 반환
        return result.stream().mapToInt(i -> i).toArray();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // 테스트 케이스
        int[] progresses1 = {93, 30, 55};
        int[] speeds1 = {1, 30, 5};
        System.out.println(Arrays.toString(sol.solution(progresses1, speeds1)));  // [2, 1]
        
        int[] progresses2 = {95, 90, 99, 99, 80, 99};
        int[] speeds2 = {1, 1, 1, 1, 1, 1};
        System.out.println(Arrays.toString(sol.solution(progresses2, speeds2)));  // [1, 3, 2]
    }
}
