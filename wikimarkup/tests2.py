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
        }
        ps = Parser()
        def _handler(bits):
            ns = bits[0].split(':')
            if ns[0] == 'wiki':
                return ['http://hoge.com',ns[1] ] 
            return bits

        ps.anchor_handler = _handler

        for (k,v) in texts.iteritems():
            p = ps.parse(k)
#            self.assertEquals(p,v )
            print k,"===>", p
        
if __name__ == '__main__':
    unittest.main()
