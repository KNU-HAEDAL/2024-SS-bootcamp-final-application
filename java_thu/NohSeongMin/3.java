import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    public Integer[] solution(int[] progresses, int[] speeds) {
	    Integer[] a = new Integer[progresses.length]; 
	     for(int i = 0; i < progresses.length; i ++) {
	    	 a[i] = (int) Math.ceil(((double)100-progresses[i]) / speeds[i]);
	    	 if(i > 0 && a[i-1] > a[i] ) a[i] = a[i-1];
	     }
	     ArrayList<Integer> b = new ArrayList<Integer>();
	     int c = 1;
	     for(int i = 1; i < progresses.length; i++) {
	    	 if(a[i-1] == a[i]) c++;
	    	 else {b.add(c); c = 1;}
	     }
	     if(c != 0 ) b.add(c);
	     return b.toArray(new Integer[b.size()]);
	     
}
}