package haedal.selenium;

import lombok.Getter;
import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@NoArgsConstructor          // 생성자를 만들지 않아도 됨
public class KNU_NoticeRepository {
    private Map<String, KNU_Notice> noticeMap = new HashMap<>();

    @Getter     // instance라는 메소드를 알아서 만들어줘라!
    private static final KNU_NoticeRepository instance = new KNU_NoticeRepository();

    public void addNotice(KNU_Notice notice) {
        noticeMap.put(notice.getTitle(), notice);
    }

    // 반환을 List<String> 이라는 것으로 한다. -> 콘솔에 출력하기 위해서
    public List<String> getAllNoticeAsString() {
        List<String> willReturn = new ArrayList<>();
//        List<KNU_Notice> noticeList = (List<KNU_Notice>) noticeMap.values();

//        for (KNU_Notice notice : noticeList){
//            String temp = "제목 : " + notice.getTitle() + "\n"
//                    + "작성자 : " + notice.getWriter() + "\n"
//                    + "작성일 : " + notice.getDate() + "\n";
//
//            willReturn.add(temp);
//        }
//        return willReturn;
//    }

        for (KNU_Notice notice : noticeMap.values()) {
            String temp = "제목 : " + notice.getTitle() + "\n"
                    + "작성자 : " + notice.getWriter() + "\n"
                    + "날짜 : " + notice.getDate() + "\n";

            willReturn.add(temp);
        }
        return willReturn;
    }

    public List<KNU_Notice> getAllNotice(){
        return (List<KNU_Notice>) noticeMap.values();
    }
}
