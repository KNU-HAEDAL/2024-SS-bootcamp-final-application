import java.util.LinkedList;
class Solution {
    boolean solution(String s) {
        LinkedList<String> stack = new LinkedList<String>();
			
	        boolean answer = true;
	        answer = stack.isEmpty();
	        for(int i = 0; i < s.length() ;i  ++) {
	        	String str = s.substring(i,i+ 1);
	        	switch (str) {
	        		case ")":{
	        			if(stack.isEmpty()) return false;
	        			stack.pop();
	        			break;
	        		}
	        		case "(":{
	        			stack.push(str);
	        			break;
	        		}
	        	}
	        }
	        if(stack.isEmpty()) answer = true;
	        else answer = false;

	        return answer;
    }
}