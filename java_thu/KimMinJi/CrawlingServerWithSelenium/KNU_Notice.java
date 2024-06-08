package haedal.selenium;

import lombok.Data;

@Data                       // 알아서 Getter, Setter을 만들어줌
public class KNU_Notice {
    private String title;   // 제목을 담을 그릇
    private String writer;  // 작성자를 담을 그릇
    private String date;    // 날짜를 담을 그릇
}
