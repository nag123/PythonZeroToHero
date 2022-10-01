from html.parser import HTMLParser
if __name__ == "__main__":



    class CustomHtmlParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            print(tag)
            for ele in attrs:
                print("->", ele[0], ">", ele[1])


    parser = CustomHtmlParser()
    for _ in range(int(input())):
        parser.feed(input())