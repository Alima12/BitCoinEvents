

class TextResponse:
    header = """"""
    footer = """"""
    content = []
    responnse = ""
    def make_content(self):
        self.responnse = ""
        text = "\n".join((self.content))
        self.responnse = header + "\n" + text + "\n" + self.footer
        return self.response
    
    def add_content(self, text):
        self.content.append(text)
        