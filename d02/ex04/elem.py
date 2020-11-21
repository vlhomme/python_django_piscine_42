class Text(str):
    def __str__(self):
        return (super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n'))

class Elem:
    def __init__(self, tag = 'div', attr = {}, content = None, tag_type = 'double'):
        self.tag = tag
        self.attr = attr
        self.content = content
        self.tag_type = tag_type

    def __str__(self):
        if self.tag_type == 'double':
            begin = '<' + self.tag + '>'
            end = '</' + self.tag + '>'
            if self.content == None:
                return begin + end
            elif isinstance(self.content, Elem):
                return begin + '\n  ' + self.content.__str__() + '\n' + end
            elif isinstance(self.content, list):
                middleString = ''
                for el in self.content:
                    if len(str(el)) > 0:
                        middleString += '\n  ' + str(el)
                return begin + middleString + '\n' + end
            elif len(str(self.content)) > 0:
                return begin + '\n  ' + str(self.content) + '\n' + end
        return ""