import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        Set<Integer> res = new HashSet<>();
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                res.add(numbers[i] + numbers[j]);
            }
        }
        
        ArrayList<Integer> sortedList = new ArrayList<>(res);
        sortedList.sort(null);
        
        int[] answer = new int[sortedList.size()];
        for (int i = 0; i < sortedList.size(); i++) {
            answer[i] = sortedList.get(i);
        }
        
        return answer;
    }
}
