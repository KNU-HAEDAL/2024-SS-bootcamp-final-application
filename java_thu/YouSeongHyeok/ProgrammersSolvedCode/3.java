import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {

        int n = progresses.length;
        int[] daysToComplete = new int[n];
        for (int i = 0; i < n; i++) {
            daysToComplete[i] = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);
        }

        List<Integer> result = new ArrayList<>();
        int count = 1;
        int currentMax = daysToComplete[0];

        for (int i = 1; i < n; i++) {
            if (daysToComplete[i] <= currentMax) {
                count++;
            } else {
                result.add(count);
                count = 1;
                currentMax = daysToComplete[i];
            }
        }

        result.add(count);

        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }

        return answer;
    }
}
