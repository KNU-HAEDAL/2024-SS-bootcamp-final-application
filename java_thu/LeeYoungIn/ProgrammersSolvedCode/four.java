import java.util.HashMap;

public class Solution {
    public String solution(String[] participant, String[] completion) {
        // 참가자 명단을 해시맵으로 생성
        HashMap<String, Integer> participantMap = new HashMap<>();
        
        // 참가자 명단을 해시맵에 추가하면서 이름의 출현 횟수를 기록
        for (String name : participant) {
            participantMap.put(name, participantMap.getOrDefault(name, 0) + 1);
        }
        
        // 완주자 명단을 해시맵에서 감소시킴
        for (String name : completion) {
            participantMap.put(name, participantMap.get(name) - 1);
        }
        
        // 완주하지 못한 선수 찾기
        for (String name : participantMap.keySet()) {
            if (participantMap.get(name) > 0) {
                return name;
            }
        }
        
        // 모든 선수가 완주한 경우는 없으므로 예외 처리 불필요
        return null;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
           System.out.println(sol.solution(new String[]{"leo", "kiki", "eden"}, new String[]{"eden", "kiki"})); // "leo"
        System.out.println(sol.solution(new String[]{"marina", "josipa", "nikola", "vinko", "filipa"}, new String[]{"josipa", "filipa", "marina", "nikola"})); // "vinko"
        System.out.println(sol.solution(new String[]{"mislav", "stanko", "mislav", "ana"}, new String[]{"stanko", "ana", "mislav"})); // "mislav"
       
}
