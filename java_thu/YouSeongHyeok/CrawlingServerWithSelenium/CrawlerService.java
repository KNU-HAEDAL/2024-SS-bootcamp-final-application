package haedal.selenium_one;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

import java.util.*;

public class KNUCrawlerService {
    KNUNoticeRepository repo = KNUNoticeRepository.getInstance();
    public void DoCrawler(){
        // 크롬 드라이버 설정
        System.setProperty("webdriver.chrome.driver", "chromedriver.exe"); // 윈도우
        // System.setProperty("webdriver.chrome.driver", "./chromedriver"); // 리눅스, 맥

        // 크롬 옵션 설정
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--remote-allow-origins=*");
        WebDriver driver = new ChromeDriver(options);

        // 공지사항 페이지 접속
        driver.get("https://www.knu.ac.kr/wbbs/wbbs/bbs/btin/stdList.action?menu_idx=42"); //바꿔야 돼

        //#btinForm > div > table > tbody
        //#btinForm > div > table > tbody > tr:nth-child(1)
        //#btinForm > div > table > tbody > tr:nth-child(11)
        //#btinForm > div > table > tbody > tr:nth-child(20)
        List<WebElement> elements = driver.findElements(By.cssSelector(("#btinForm > div > table > tbody")));
        // 공지사항 목록을 가져옵니다.
        int count  = 1;
        for(int i = 11 ; i < 21 ; i++){

            KNUNotice notice = new KNUNotice();

            WebElement middle = driver.findElement(By.cssSelector("tr:nth-child(" + i + ")"));
            WebElement titleSelector = middle.findElement(By.cssSelector(".subject"));
            notice.setTitle(titleSelector.getText());

            notice.setDate(middle.findElement(By.cssSelector(".date")).getText());
            notice.setWriter(middle.findElement(By.cssSelector(".writer")).getText());

            repo.addNotice(notice);
        }

        // WebDriver 종료
        driver.quit();

        // NoticeDto 리스트 반환
//        return notices;
    }
}
