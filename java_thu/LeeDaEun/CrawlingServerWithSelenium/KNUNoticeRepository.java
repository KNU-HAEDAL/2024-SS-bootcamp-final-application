package haedal.selenium;

import lombok.Getter;
import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
@NoArgsConstructor

public class KNUNoticeRepository {
    private Map<String, KNUNotice> noticeMap = new HashMap<>();

    @Getter
    private static KNUNoticeRepository instance = new KNUNoticeRepository();

    public void addNotice(KNUNotice notice){
        noticeMap.put(notice.getTitle(), notice);
    }

    //반환을 List<String> 이라는 것으로 한다 -> 콘솔에 출력하기 위해서
    public List<String> getAllNoticeAsString() {
        List<String> willReturn = new ArrayList<>();

        List<KNUNotice> noticeList = (List<KNUNotice>) noticeMap.values();

        for (KNUNotice notice : noticeList) {
            String temp = "제목 : " + notice.getTitle() + "\n"
                    + "작성자 : " + notice.getWriter() + "\n"
                    + "작성일 : " + notice.getDate() + "\n";
            willReturn.add(temp);
        }

        return willReturn;
    }

    public List<KNUNotice> getAllNotice() {
        return (List<KNUNotice>) noticeMap.values();
    }

}
