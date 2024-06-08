package haedal.selenium;

import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

@NoArgsConstructor
public class KNUNoticeRepository {
    private Map<String, KNUNotice> noticeMap = new HashMap<>();

    private static KNUNoticeRepository instance = new KNUNoticeRepository();

    public static KNUNoticeRepository getInstance() {
        return instance;
    }

    public void addNotice(KNUNotice notice) {
        noticeMap.put(notice.getTitle(), notice);
    }

    //반환 : List<String> :: 콘솔에 출력을 위해
    public List<String> getAllNoticeAsString() {
        List<String> willReturn = new ArrayList<>();
        List<KNUNotice> noticeList = (List<KNUNotice>) noticeMap.values();

        for(KNUNotice notice : noticeList) {
            String temp = "제목 : " + notice.getTitle() + "\n"
                    + "작성자 : " + notice.getWriter() + "\n"
                    + "날짜 : " + notice.getDate() + "\n";

            willReturn.add(temp);
        }

        return willReturn;
    }

    public List<KNUNotice> getAllNotice() {
        return (List<KNUNotice>) noticeMap.values();
    }
}
