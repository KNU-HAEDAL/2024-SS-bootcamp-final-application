import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        
        Set<Integer> resultSet = new HashSet<>();
        
        
        for (int i = 0; i < numbers.length - 1; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                resultSet.add(numbers[i] + numbers[j]);
            }
        }
        
        // Set을 List로 변환 오름차순으로 정렬
        List<Integer> resultList = new ArrayList<>(resultSet);
        Collections.sort(resultList);
        
        // 리스트를 배열로 변환
        int[] answer = new int[resultList.size()];
        for (int i = 0; i < resultList.size(); i++) {
            answer[i] = resultList.get(i);
        }
        return answer;
    }
}
