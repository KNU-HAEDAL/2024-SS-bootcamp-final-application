import java.util.*;

public class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        // 각 기능이 완료되는 데 걸리는 일수를 계산하는 리스트
        List<Integer> daysList = new ArrayList<>();
        
        // 각 기능에 대해 완료 일수를 계산
        for (int i = 0; i < progresses.length; i++) {
            int days = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);
            daysList.add(days);
        }
        
        // 배포마다 몇 개의 기능이 배포되는지를 저장하는 리스트
        List<Integer> deployCounts = new ArrayList<>();
        
        // 배포의 기준이 되는 첫 번째 기능의 완료 일수
        int deployDay = daysList.get(0);
        int count = 1;
        
        // 두 번째 기능부터 끝까지 비교
        for (int i = 1; i < daysList.size(); i++) {
            if (daysList.get(i) <= deployDay) {
                // 현재 기능이 기준 날짜보다 작거나 같으면 같은 배포 그룹에 포함
                count++;
            } else {
                // 새로운 배포 그룹 시작
                deployCounts.add(count);
                deployDay = daysList.get(i);
                count = 1;
            }
        }
        
        // 마지막 배포 그룹 추가
        deployCounts.add(count);
        
        // 결과를 int 배열로 변환
        int[] result = new int[deployCounts.size()];
        for (int i = 0; i < deployCounts.size(); i++) {
            result[i] = deployCounts.get(i);
        }
        
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
         System.out.println(Arrays.toString(sol.solution(new int[]{93, 30, 55}, new int[]{1, 30, 5}))); // [2, 1]
        System.out.println(Arrays.toString(sol.solution(new int[]{95, 90, 99, 99, 80, 99}, new int[]{1, 1, 1, 1, 1, 1}))); // [1, 3, 2]
    }
}
