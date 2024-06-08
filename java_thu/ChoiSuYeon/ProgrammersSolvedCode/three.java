import java.util.*;

public class three {
    public String solution(String[] participant, String[] completion) {
        String answer = "";

//         List<String> Uncompletion = new ArrayList<>(Arrays.asList(participant));

//         for (int i = 0; i < completion.length; i++)
//             Uncompletion.remove(completion[i]);

//         answer = Uncompletion.get(0);

        Map<String, Integer> Uncompletion = new HashMap<>();

        for (String p : participant)
            Uncompletion.put(p, Uncompletion.getOrDefault(p, 0) + 1);

        for (String c : completion)
            Uncompletion.put(c, Uncompletion.get(c) - 1);

        for (Map.Entry<String, Integer> entry : Uncompletion.entrySet())
            if (entry.getValue() != 0) {
                answer = entry.getKey();
                break;
            }

        return answer;
    }
}