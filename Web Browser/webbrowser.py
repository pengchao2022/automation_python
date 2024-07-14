

from tkinter import * # pip install tk-tools
import tkinterweb # type: ignore # pip install tkinterweb
import sys

class Browser(Tk):
    def __init__(self):
        super(Browser,self).__init__()
        self.title("Pengchao Web Browser")
        try:
            browser = tkinterweb.HtmlFrame(self)
            browser.load_website("www.baidu.com")
            browser.pack(fill="both",expand=True)
        except Exception:
            sys.exit()
            
            
def main():
    browser = Browser()
    browser.mainloop()
    
if __name__ == "__main__":
    # Webbrowser v1.0
    main()
