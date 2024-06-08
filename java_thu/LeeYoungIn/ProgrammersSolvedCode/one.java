import java.util.*;

public class Solution {
    public int[] solution(int[] numbers) {
        // 합을 저장할 HashSet 생성
        Set<Integer> sums = new HashSet<>();
        
        // 이중 반복문을 사용하여 모든 두 수의 조합을 선택
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                sums.add(numbers[i] + numbers[j]);
            }
        }
        
        // HashSet을 ArrayList로 변환하고 정렬
        List<Integer> sortedSums = new ArrayList<>(sums);
        Collections.sort(sortedSums);
        
        // 정렬된 결과를 배열로 변환
        int[] result = new int[sortedSums.size()];
        for (int i = 0; i < sortedSums.size(); i++) {
            result[i] = sortedSums.get(i);
        }
        
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        // 테스트 예시
        System.out.println(Arrays.toString(sol.solution(new int[]{2, 1, 3, 4, 1}))); // [2, 3, 4, 5, 6, 7]
        System.out.println(Arrays.toString(sol.solution(new int[]{5, 0, 2, 7})));    // [2, 5, 7, 9, 12]
    }
}
