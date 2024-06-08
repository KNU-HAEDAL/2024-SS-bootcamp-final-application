import java.util.Stack;

public class Solution {
    public boolean solution(String s) {
        // 스택을 사용하여 괄호를 확인
        Stack<Character> stack = new Stack<>();
        
        // 문자열의 각 문자에 대해 처리
        for (char c : s.toCharArray()) {
            if (c == '(') {
                // 여는 괄호를 스택에 추가
                stack.push(c);
            } else if (c == ')') {
                // 닫는 괄호가 나왔을 때 스택이 비어 있으면 false
                if (stack.isEmpty()) {
                    return false;
                }
                // 스택에서 여는 괄호를 하나 제거
                stack.pop();
            }
        }
        
        // 모든 처리가 끝났을 때 스택이 비어 있으면 올바른 괄호
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        // 테스트 예시
        System.out.println(sol.solution("()()"));    // true
        System.out.println(sol.solution("(())()")); // true
        System.out.println(sol.solution(")()("));   // false
        System.out.println(sol.solution("(()("));   // false
    }
}
