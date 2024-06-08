import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = {};

        // 모든 가능한 조합을 구함
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < numbers.length - 1; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                int sum = numbers[i] + numbers[j];
                if (!list.contains(sum)) { // 중복된 수는 제외
                    list.add(sum);
                }
            }
        }

        // ArrayList를 배열로 변환
        answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }

        // 오름차순 정렬
        Arrays.sort(answer);

        return answer;
    }
}
