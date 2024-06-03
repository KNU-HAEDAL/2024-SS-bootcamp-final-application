package haedal.selenium_one;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class KNUCrawlerController {

    KNUNoticeRepository repo = KNUNoticeRepository.getInstance();

    @ResponseBody
    @GetMapping("knu-notice")
    public List<KNUNotice> Crawler(){
        KNUCrawlerService service = new KNUCrawlerService();

        service.DoCrawler();

        List<String> notices = repo.getAllNoticeAsString();
        for(String notice : notices){
            System.out.println(notice);
        }
        return repo.getAllNotice();
    }
}
