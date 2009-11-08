import unittest

from parser import parse,parselite,Parser

class WikimarkupTestCase(unittest.TestCase):

    def testLinks(self):
         
        texts= {
                "[http://mydomain.com/ mydomain.com]" : '<p><a href="http://mydomain.com/">mydomain.com</a>\n</p>',
                "[http://mydomain.com/]" : '<p><a href="http://mydomain.com/">http://mydomain.com/</a>\n</p>',
                "[mydomain.com/]" :  '<p>[mydomain.com/]\n</p>',
                "[/hello/world]" : '<p><a href="/hello/world">/hello/world</a>\n</p>',
                "[wiki:hello]" : "",
                "[mailto:hello@hdknr.com]" : '<p><a href="mailto:hello">mailto:hello</a>\n</p>',
                "[ilink:http://www.micrsoft.com:http://www.image.om/test.gif  afdsafdas]" :"",
        }
        ps = Parser()
        default_handler = ps.bracket_handler
        def _handler(bits):
            ns = bits[0].split(':')
            if ns[0] == 'wiki':
                return ['<a href="','http://hoge.com/+ns[1]','">',ns[1],'</a>']
            if ns[0] == 'ilink':
                return  ['<a href="','%s:%s'%(ns[1],ns[2]),'">','<img src="%s:%s">'%(ns[3],ns[4]),'</a>']
            return default_handler(bits)
            

        ps.bracket_handler = _handler

        for (k,v) in texts.iteritems():
            p = ps.parse(k)
#            self.assertEquals(p,v )
            print k,"===>", p
        
if __name__ == '__main__':
    unittest.main()
