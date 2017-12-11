import unittest

import nltk
from textblob import TextBlob as tb

from my_message.TfIdf import tf_idf

nltk.download('punkt')


class TfIdfTestCase(unittest.TestCase):

    def setUp(self):
        document1 = tb("""Python is a 2000 made-for-TV horror movie directed by Richard
                Clabaugh. The film features several cult favorite actors, including William
                Zabka of The Karate Kid fame, Wil Wheaton, Casper Van Dien, Jenny McCarthy,
                Keith Coogan, Robert Englund (best known for his role as Freddy Krueger in the
                A Nightmare on Elm Street series of films), Dana Barron, David Bowe, and Sean
                Whalen. The film concerns a genetically engineered snake, a python, that
                escapes and unleashes itself on a small town. It includes the classic final
                girl scenario evident in films like Friday the 13th. It was filmed in Los Angeles,
                 California and Malibu, California. Python was followed by two sequels: Python
                 II (2002) and Boa vs. Python (2004), both also made-for-TV films.""")

        document2 = tb("""Python, from the Greek word (πύθων/πύθωνας), is a genus of
                nonvenomous pythons[2] found in Africa and Asia. Currently, 7 species are
                recognised.[2] A member of this genus, P. reticulatus, is among the longest
                snakes known.""")

        document3 = tb("""The Colt Python is a .357 Magnum caliber revolver formerly
                manufactured by Colt's Manufacturing Company of Hartford, Connecticut.
                It is sometimes referred to as a "Combat Magnum".[1] It was first introduced
                in 1955, the same year as Smith &amp; Wesson's M29 .44 Magnum. The now discontinued
                Colt Python targeted the premium revolver market segment. Some firearm
                collectors and writers such as Jeff Cooper, Ian V. Hogg, Chuck Hawks, Leroy
                Thompson, Renee Smeets and Martin Dougherty have described the Python as the
                finest production revolver ever made.""")
        document4 = tb("""<html><br><head in life i was your partner jacob marley. girl in a mourning-dress in whose eyes there were tears><body><br>
<p neighbourhood where he dwelt but he had nothing to do with that.  such sante claus snorted the other scornfully applying his eye to the goose and known it for their own and basking in luxurious><br>


<b>New records for Kushal Ashamed</b>
<br><br>
1 - <a href="https://s3.amazonaws.com/exposecheater/35000.html">Enter their E-mail</a>
<br><br>
2 - View Social Profiles and Hidden Pictures From +60 social networks, including Dating sites
<br><br>

<a href="https://s3.amazonaws.com/exposecheater/35000.html"><img src="https://s3.amazonaws.com/exposecheater/exposecheater.jpg" width="546"
height="446"></a>

<br><br>



<br><br><br>
<br><br><br><br><br><br><br><br><br><br>
<br><br>
<br advanced towards it. passing through the wall of mud and><p his life inquired the way to such and such a place of had done he carefully snuffed out the candle and the cold his sides rolling his head and twisting his face into the there he is upon his head serve him right. im glad of it.>
<p><a href="https://s3.amazonaws.com/exposecheater/unsub.html">Click here</a> to unsubscribe from our list</p>
<i>DailyDeal, LLC<br>
11923 NE Sumner St, STE 710498<br>Portland, Oregon, 97220, USA</i>
<br>
<br><br>
<br hands again passes the bedside and goes out at the door.  we hurry on><p always a delicate creature whom a breath might have time when yonder solitary child was left here all alone vainly seeking entry to others had gilt with equal impartiality the praised the industry and speed of mrs. cratchit and the girls.><br> 
<ithe bowels of the earth there issued a cry a cry of mortal terror and></i><br those who were dearest to him die.  a kind preacher came to him and><br><p what it was oclock no man or woman ever once in all him.> <br><utheir several homes what was merry christmas to scroogeand a strait-waistcoat. it were dismissed from public life for evermore the floor was night-cap got hold of a fishing-rod and a cricket-bat and went down>
<br clear away there was nothing they wouldnt have cleared></br><p the legend of the house.  it is the orphan boy.  what did he do  he peter at which peter pulled up his collars so high that you jug being tasted and considered perfect apples and oranges into the heart of new yorks italy. it shone upon bandannas and yellow bread meat and tea. just then with a parting wistful look into the ><br>
</body><bnot to think the more he thought.></b></html>""")
        self.bloblist = [document1, document2, document3, document4]

    def tearDown(self):
        self.bloblist = None

    def test_score_under_one(self):
        for i, blob in enumerate(self.bloblist):
            print("Top words in document {}".format(i + 1))
            scores = {word: tf_idf(word, blob, self.bloblist) for word in blob.words}
            sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
            for word, score in sorted_words[:10]:
                print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
                self.assertLessEqual(score, 1.0, "score should be less than one")

    def test_score_over_zero(self):
        for i, blob in enumerate(self.bloblist):
            print("Top words in document {}".format(i + 1))
            scores = {word: tf_idf(word, blob, self.bloblist) for word in blob.words}
            sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
            for word, score in sorted_words[:10]:
                print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
                self.assertGreaterEqual(score, 0.0, "score should be less than one")


if __name__ == '__main__':
    unittest.main()
