package ProgrammersSolvedCode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class OwnSolution {
    public int[] solution(int[] numbers) {
        List<Integer> resultList = new ArrayList<>();
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                int sum = numbers[i] + numbers[j];
                if (!resultList.contains(sum)) { // Check for duplicates
                    resultList.add(sum);
                }
            }
        }

        int[] result = resultList.stream().mapToInt(Integer::intValue).toArray();
        Arrays.sort(result);
        return result;
    }
}
