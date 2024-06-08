package haedal.selenium;

import java.util.*;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class KNUCrawlerController {
    KNUNoticeRepository repo = KNUNoticeRepository.getInstance();

    @ResponseBody
    @GetMapping ("knu-notice")
    public List<KNUNotice> Crawler() {
        KNUCrwalerService service = new KNUCrwalerService();

        service.DoCrawler();

        List<String> notices = repo.getAllNoticeAsString();
        for(String notice : notices) {
            System.out.println(notice);
        }

        return repo.getAllNotice();
    }
}

