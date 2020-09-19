import unittest
import sys
import os

sys.path.append(os.path.abspath('..'))

from lib import shorten_text as s  # noqa: E402


class TestShortenText(unittest.TestCase):

    def test_shorten_text_long(self):
        long_text = '菅新政権が１６日発足した。安倍前政権の継承と「国民のために働く内閣」を掲げ、\
新型コロナウイルス感染の収束と経済再生に全力を挙げるとしている。ただ最大の焦点が、\
菅義偉首相がいつ衆院解散・総選挙に踏み切るのかにあるのは、論をまたない。'

        expect = '菅新政権が１６日発足した。安倍前政権の継承と「国民のために働く内閣」を掲げ、新型コロナウイルス感染の'
        result = s.shorten_text(long_text, 50)
        self.assertEqual(expect, result)

    def test_shorten_memo_short(self):
        long_text = 'ドルチェ＆ガッバーナの香水が思い出させる'

        expect = 'ドルチェ＆ガッバーナの香水が思い出させる'
        result = s.shorten_text(long_text, 50)
        self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()
