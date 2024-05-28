import java.util.Stack;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Stack<Character> stack = new Stack<>();
        char[] arr = s.toCharArray();
        for (char comp : arr) {
            if (comp == '(') {
                stack.push(comp);
            } else if (!stack.empty() && comp == ')') {
                stack.pop();
            } else {
                stack.push(comp);
            }
        }
        if (!stack.empty()) {
            answer = false;
        }

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("Hello Java");

        return answer;
    }
}