import java.util.ArrayList;
class Solution {
    public int[] solution(int[] numbers) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        for(int i = 0; i < numbers.length; i++){
            for(int j = i+1; j < numbers.length; j++){
                if(!res.contains(numbers[i] + numbers[j])) {
                     res.add(numbers[i] + numbers[j]);
                }
            }
        }
        res.sort(null);
        int[] answer = new int[res.size()];
        for(int i = 0 ;i < res.size(); i++){
            answer[i] = res.get(i);
        }
        return answer;
    }
    
}