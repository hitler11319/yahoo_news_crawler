import unittest
import news
import web

class News_mathod_test(unittest.TestCase):
    def setUp(self):
        self.news = news.List_news()


    def test_append(self):
        test_input = "this is test input"
        self.assertEqual(self.news.append(test_input), ["this is test input"])

    def test_filter(self):
        self.news.append("123")
        self.news.append("456")
        self.news.append("7893")
        total = ""
        goal = "3"
        for i in self.news.filter(lambda item: goal in item):
            total += i
        self.assertEqual(total, "1237893")

    def test_change_time_format(self):
        date = "2015年12月20日 下午3:12"
        self.assertEqual(web.change_time_format(date), "2015年12月20日 下午15:12")

    def test_dealstr(self):
        url = ["<a href=\"/405964.html class=\"hello\"  ", "<a href=\"/66482.html class=\"hello\"", "<a href=\"/11158.html class=\"hello\""]
        self.assertEqual(web.dealstr(url), ["405964.", "66482.", "11158."])

if __name__ == '__main__':
    unittest.main()
