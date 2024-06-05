package haedal.selenium_one;

import lombok.Getter;
import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@NoArgsConstructor
public class KNUNoticeRepository {
    private Map<String, KNUNotice> knuStorage = new HashMap<>();

    @Getter
    private static KNUNoticeRepository instance = new KNUNoticeRepository();
    public void addNotice(KNUNotice notice){
        knuStorage.put(notice.getTitle(), notice);
    }
    public List<String> getAllNoticeAsString(){
        List<String> willReturn = new ArrayList<>();
        List<KNUNotice> noticeList = (List<KNUNotice>) knuStorage.values();
        for(KNUNotice notice : noticeList){
            String temp = "제목 : " + notice.getTitle() + "\n"
                    + "작성자 : " + notice.getWriter() + "\n"
                    + "작성일 : " + notice.getDate();
        }

        return willReturn;
    }
    public List<KNUNotice> getAllNotice(){
        return (List<KNUNotice>) knuStorage.values();
    }

}
