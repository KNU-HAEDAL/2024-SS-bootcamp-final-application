import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answerList = new ArrayList<>();
        int day = 0; // 개발이 완료되는 날짜
        
        // 각 기능의 개발 완료까지 걸리는 일수 계산
        for (int i = 0; i < progresses.length; i++) {
            int remain = 100 - progresses[i]; // 남은 진도
            int devDays = remain / speeds[i]; // 개발 완료까지 걸리는 일수
            if (remain % speeds[i] != 0) devDays++; // 남은 진도가 있으면 하루를 더해줌
            if (devDays > day) {
                // 새로운 기능의 개발이 더 오래 걸리는 경우 배포
                answerList.add(1);
                day = devDays;
            } else {
                // 같은 날에 개발이 완료되는 경우 배포
                int lastIndex = answerList.size() - 1;
                answerList.set(lastIndex, answerList.get(lastIndex) + 1);
            }
        }
        
        // List를 배열로 변환
        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }
        
        return answer;
    }
}
