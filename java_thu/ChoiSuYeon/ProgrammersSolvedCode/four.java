import java.util.*;

public class four {
    public static String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> map = new HashMap<>();

        // 참가자 명단을 HashMap에 추가
        for (String p : participant) {
            map.put(p, map.getOrDefault(p, 0) + 1);
        }

        // 완주자 명단을 통해 HashMap에서 갱신
        for (String c : completion) {
            map.put(c, map.get(c) - 1);
        }

        // 값이 0이 아닌 참가자를 찾음
        for (String key : map.keySet()) {
            if (map.get(key) != 0) {
                return key;
            }
        }

        return null; // 모든 참가자가 완주한 경우
    }
}