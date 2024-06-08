package haedal.selenium;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class KNU_CrawlerController {
    KNU_NoticeRepository repo = KNU_NoticeRepository.getInstance();

    @ResponseBody
    @GetMapping("knu-notice")
    public List<KNU_Notice> Crawler() {
        KNU_CrawlerService service = new KNU_CrawlerService();

        service.DoCrawler();

        List<String> notices = repo.getAllNoticeAsString();
        for (String notice : notices) {
            System.out.println(notice);
        }

        return repo.getAllNotice();
    }
}
