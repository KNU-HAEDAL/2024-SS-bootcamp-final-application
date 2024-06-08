package ProgrammersSolvedCode;

import java.util.ArrayList;
import java.util.List;

class ThreeSolution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answerList = new ArrayList<>();
        int days = 0;
        int count = 0;

        while (progresses.length > 0) {
            if (progresses[0] + days * speeds[0] >= 100) {
                progresses = removeElement(progresses);
                speeds = removeElement(speeds);
                count++;
            } else {
                if (count > 0) {
                    answerList.add(count);
                    count = 0;
                }
                days++;
            }
        }

        if (count > 0) {
            answerList.add(count);
        }

        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }

        return answer;
    }

    private int[] removeElement(int[] arr) {
        int[] newArr = new int[arr.length - 1];
        System.arraycopy(arr, 1, newArr, 0, newArr.length);
        return newArr;
    }
}