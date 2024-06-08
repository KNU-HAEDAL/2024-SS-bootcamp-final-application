import java.util.*;     // Arrays 사용

public class one {
    public int[] solution(int[] numbers) {
        //int[] answer = {};
        int[] answer = new int[numbers.length * (numbers.length - 1)  / 2];
        // answer에 값을 넣기 위해서는 크기 설정 해주어야함

        // HashSet : 중복을 허용하지 않는 배열
        HashSet<Integer> iHS = new HashSet<>();
        // HashSet 생성 : <> 안에 변수형, new HashSet은 <>와 () 안의 값 생략 가능

        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                int sum = numbers[i] + numbers[j];
                iHS.add(sum);
            }
        }
        answer = new int[iHS.size()];       // answer 배열의 크기를 HashSet의 크기로 재선언

        int idx = 0;
        for (int n : iHS) {
            answer[idx++] = n;             // HashSet에 있는 값을 answer에 입력
        }
        Arrays.sort(answer);

        return answer;
    }
}