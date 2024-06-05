import java.util.HashMap;

public class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> map = new HashMap<>();

        // 참가자 명단에 있는 선수들을 해시맵에 추가
        for (String p : participant) {
            // 동명이인이 있을 수 있으므로, 이름이 같은 선수들의 수를 저장
            map.put(p, map.getOrDefault(p, 0) + 1);
        }

        // 완주자 명단에 있는 선수들을 해시맵에서 제거
        for (String c : completion) {
            map.put(c, map.get(c) - 1);
        }

        // 완주하지 못한 선수의 이름을 반환
        for (String key : map.keySet()) {
            if (map.get(key) != 0) {
                return key;
            }
        }

        return "";
    }
}