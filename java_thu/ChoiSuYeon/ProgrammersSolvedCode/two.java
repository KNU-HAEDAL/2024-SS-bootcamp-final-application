import java.util.*;

public class two {
    boolean solution(String s) {
        boolean answer = true;
        int idx = 0;

        Stack<Character> stack = new Stack<>();

        char[] arrayS = s.toCharArray();
        //System.out.println(arrayS);

        for (int i = 0; i < arrayS.length; i++) {
            if (arrayS[i] == '(') {
                stack.push(arrayS[i]);
            } else if (arrayS[i] == ')') {
                if (stack.isEmpty()) {
                    answer = false;
                    return answer;
                }
                stack.pop();
            }
        }

        if (!stack.isEmpty())
            answer = false;

        return answer;
    }
}