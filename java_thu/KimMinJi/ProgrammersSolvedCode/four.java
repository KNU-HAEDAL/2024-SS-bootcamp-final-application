import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";

        // 참가자 이름과 그 출현 빈도수를 저장하는 HashMap 생성
        HashMap<String, Integer> map = new HashMap<>();
        
        // 참가자 명단을 HashMap에 추가
        for (String name : participant) {
            map.put(name, map.getOrDefault(name, 0) + 1);
        }
        
        // 완주자 명단에서 참가자를 제거
        for (String name : completion) {
            map.put(name, map.get(name) - 1);
        }
        
        // 남은 참가자를 확인하여 완주하지 못한 선수를 찾음
        for (String name : map.keySet()) {
            if (map.get(name) != 0) {
                answer = name;
                break;
            }
        }
        
        return answer;
    }
}
