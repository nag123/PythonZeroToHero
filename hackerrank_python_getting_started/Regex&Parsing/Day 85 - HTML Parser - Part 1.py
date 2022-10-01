#please change the import statement FROM : from HTMLParser import HTMLParser ==> from html.parser import HTMLParser
from html.parser import HTMLParser

if __name__ == "__main__":
    # create a subclass and override the handler methods
    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            print(f"Start : {tag}")
            for a, b in attrs:
                print(f"-> {a} > {b}")

        def handle_endtag(self, tag):
            print(f"End   : {tag}")


        def handle_startendtag(self, tag, attrs):
            print(f"Empty : {tag}")
            for a, b in attrs:
                print(f"-> {a} > {b}")


    # enter the number of lines
    n = int(input())
    htmlbodyasstring = ""
    for i in range(n):
        inputfromuser = input()
        #append it to a string and pass it as a stretch
        htmlbodyasstring += inputfromuser
    parser = MyHTMLParser()
    parser.feed(htmlbodyasstring)