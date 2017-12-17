import unittest

from my_message import MyParser


class TfIdfTestCase(unittest.TestCase):

    def setUp(self):
        document = """<br><br>
  <a href="https://s3.amazonaws.com/b2asiandating1/35000.html">View my Pics Now. It's
Free!</a><br><br>

         
<a href="https://s3.amazonaws.com/b2asiandating1/35000.html"><img src="https://s3.amazonaws.com/b2asiandating1/asian.jpg" border="0"
height="497"
width="623"></a>



<br><br><br>
We wait your news!<br>
Naoma
 
<br><br><br><br><br><br><br><br><br><br>
<br>

<p><a href="https://s3.amazonaws.com/b2asiandating1/unsub.html">Click here</a> to unsubscribe from our list</p>
<i>DailyDeal, LLC<br>
11923 NE Sumner St, STE 710498<br>Portland, Oregon, 97220, USA</i>
<br><br>
<br><br><br><br>
<br bereavement by pointing out to him that i was only a superfluous><p if age be hiding for me in the unseen portion of thy downward growth o wasnt cried bob for the sake of anything he might be entire life so far i may saythat i hope you have been glad to hear of pictured the changes that were to come upon our lives and merrily><br><br> <ialways of standing well in their esteem in a business point></i><br the boy as he had lost the child and after calling to him in vain went><br><br><p its from sante claus he said laying it on the coffin. nibsy after tea they had some music. for they were a musical> <br><br><ufollowing the finger read upon the stone of the neglected
trembled more when he said that tiny tim was growing the prospect.  on the hill-side beyond the shapelessly-diffused town and>
<br must be near his time.></br>
<p counting-house the day before and said scrooge and marleys i business to collect it as easily as they could. it was everybodys meeting anything until at last he came to a beautiful child.  so he said spirit. he was not the dogged scrooge he had been and hand was open generous and true the heart brave warm ><br><br>
</body><bthere are flaming logs heaped high there are joyful faces there is></b></html>"""
        self.document = document

    def tearDown(self):
        self.document = None

    def test_score_under_one(self):
        s = MyParser.MyParser()
        s.feed(self.document)
        result = s.get_data()
        print(result)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
