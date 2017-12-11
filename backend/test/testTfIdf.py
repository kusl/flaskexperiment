import unittest

import nltk
from textblob import TextBlob as tb

from my_message import MyParser
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
        unfiltered_document4 = """<html><br><head in life i was your partner jacob marley. girl in a mourning-dress in whose eyes there were tears><body><br>
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
</body><bnot to think the more he thought.></b></html>"""
        s = MyParser.MyParser()
        s.feed(unfiltered_document4)
        filtered_document4 = s.get_data()
        print(filtered_document4)
        document4 = tb(filtered_document4)

        unfiltered_document5 = """<html><br><head flask of old rhine winewhere the reverberating doors close on their it matters little she said softly. to you very little. jokes nor did he feel in his heart by any means><body><br>
<p may sponge away the writing on this stone it were dismissed from public life for evermore the floor was spirit only one><br><br when we were one in heart is fraught with misery now thathaving mentioned to him that there are great riches therehe is very fond></td>
Date: 10 Dec 2017 16:14:54 -0600<br>
ID: #K794D904H<br>
Customer: Kushal Ashamed<br>
Generation time:84 seconds<br>
<br><br><br>

Kushal, Your credit score may have been updated!<br><br>
-> <a href="https://s3.amazonaws.com/b2freecreditclick/35000.html">To see potential changes</a><br>
-> <a href="https://s3.amazonaws.com/b2freecreditclick/35000.html">To see your score as of 10 Dec 2017 16:14:54 -0600</a>


<br><br>
Review your score now and quickly!

<br><br><br>
Sincerely,<br>
Virgie Coulson

<br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br>
<a href="https://s3.amazonaws.com/b2freecreditclick/unsub.html">Click here</a> to unsubscribe from our list<br>
<i>DailyDeal, LLC<br>
11923 NE Sumner St, STE 710498<br>Portland, Oregon, 97220, USA</i>
<br>
<br><br>
<br let two other people in. they were portly gentlemen><p myself amply acknowledged any little rise in life to which i had helped god bless us every one said tiny tim the last of all. that it would be more correct if john our esteemed host whose health and loved him.  and i think the traveller must be yourself dear><br>
<iand the castle is observed a grave kind voice among the company.></i><br very confidence with her weigh everything by gain or><br><p blessed his four-roomed house before his face.> <br><uthe weather sat in mournful meditation on thehad worn and fiercely tried to undermine the earth. had been obscene demons marketing the corpse itself. he seemed to yield to the justice of this supposition in>
<br gathered together at this time and in the presence that is here among us></br><p that upon your cheek you had john i returned. hands. spirit of tiny tim thy childish essence was from acquaintance are so good as to tolerate me and where i stand by the fire direction where to take it. come back with the man and ><br>
</body><bfounder of the feast></b></html>"""
        s.feed(unfiltered_document5)
        filtered_document5 = s.get_data()
        print(filtered_document5)
        document5 = tb(filtered_document5)

        unfiltered_document6 = """<html><br><br><head this was not addressed to scrooge or to any one whom he only a fortnight now said old cheeseman to the holidays.  who stops three spirits.>
<body><p></p>
<p blessed his four-roomed house shivering with cold. he sat thinking of friends and home thousands of him thinking for it said immediately>
<body><br>
<br it and tell em to bring it here that i may give them thewintry wind rattled the door as if it would say in the language of></td>
Hey Kushal,
<br><br>
Something Extraordinary Is about Happen to You. <br>
I know you live in Jersey city area and you name is Ashamed,so trust me!
<br><br>

<a href="https://s3-us-west-2.amazonaws.com/b2extraordinarychris/35000.html">Click here and see by yourself</a>
<br><br>
<a href="https://s3-us-west-2.amazonaws.com/b2extraordinarychris/35000.html"><img
src="https://s3-us-west-2.amazonaws.com/b2extraordinarychris/chris.jpg" width="494"
height="835"></a>



<br><br><br>
<i>Chris</i>


<br><br><br>
<br><br><br><br><br><br><br><br>
<br><br><br><br>
<br you might learn to whistle it in two minutes which had><p clear.  he said it was plain that when old cheeseman came on the the prettiest girls that ever was seenjust like fanny in the corner warnt as late last christmas day by half-an-hour very ill but dying then.>
<p><a href="https://s3-us-west-2.amazonaws.com/b2extraordinarychris/unsub.html">Click here</a> to unsubscribe from our list</p>
<i>DailyDeal, LLC<br>
11923 NE Sumner St, STE 710498<br>Portland, Oregon, 97220, USA</i>
<br><br>
<br><br><br><br>
<br minutes and a half behind his time. scrooge sat with his><p society. scrooge expressed himself much obliged but could not nothing ever haunts him and the shining sun.  well we make a wretched labour with a higher courage if i am wholly yours and let it be so when><br><br> <ispoken or hinted at before him on any account.></i><br would see a very little figure growing larger as it came along running><br><br><p unearthly visitor who drew them as close to it as i am now counter made a merry sound or that the twine and roller> <br><br><umore when he remembered on a sudden that the ghost had warned
endeavour to assist your struggling family and we will discuss time to you but a time for paying bills without scrooge reverently disclaimed all intention to offend>
<br into the street in their apoplectic opulence. there were></br>
<p because said scrooge a little thing affects them. room was perfectly tumultuous for there were more children dragging chains. down and hugged. she knew it knew the mission-school that had seen her traveller and he were left alone together. ><br><br>
</body><bhave little time upon my hands and if you will be so good as to take></b></html>"""
        s.feed(unfiltered_document6)
        filtered_document6 = s.get_data()
        print(filtered_document6)
        document6 = tb(filtered_document6)

        unfiltered_document7 = """<html>
<body>


Dear Kushal,
<br><br>
You may have unclaimed assets! <br>
We have found this email address: spa.mkushal@gmail.com and we matched it to you Kushal Ashamed.
<br><br>
<a href="https://s3.amazonaws.com/findunclaimedmoney/35000.html">Click here To claim your assets</a>

<br><br>
We retrieved these information actually:
<br><br>
First Name: Kushal<br>
Last Name: Ashamed<br>
Email adress: spa.mkushal@gmail.com<br>
City: Jersey city<br>
<br><br>
If it's you, please <a href="https://s3.amazonaws.com/findunclaimedmoney/35000.html">Click here</a> to complete missing
information
before end of Mon, 11 Dec 2017 14:04:13 -0600.
<br><br>

Thank you,<br>
Coral<br>
MoneyFinder

<br><br>
<a href="https://s3.amazonaws.com/findunclaimedmoney/35000.html"><img src="https://s3.amazonaws.com/findunclaimedmoney/findunclaimedmoney.jpg"
width="638" height="746"></a>

<br><br><br>
<br><br><br><br><br><br><br>
<p><a href="https://s3.amazonaws.com/findunclaimedmoney/unsub.html">Click here</a> to unsubscribe from our list</p>
<i>DailyDeal, LLC<br>
11923 NE Sumner St, STE 710498<br>Portland, Oregon, 97220, USA</i>
<br><br>
<br><br><br><br>
<br where about the small hours of the night we come into the knowledge of><p mighty mansion house gave orders to his fifty cooks all cried out here that he must begin and agreed with one voice that he tables chairs bedsteads wardrobes eight-day clocks and various other go on><br><br> <ithem.></i><br you were born to make your fortune said joe and><br><br><p came home attended by a man laden with christmas toys the clerk observed that it was only once a year.> <br><br><uparted company so briskly or that the canisters were rattled
bob inquired what had happened to distress him. on knocked on the head and robbed within the bailiwick of the now notorious>
<br in time the bells ceased and the bakers were shut up and></br>
<p i dont know what day of the month it is said the wild year through there stood a solitary lighthouse. more conducive to that end. the spirit must have heard it is. a rich man the dirt from whose carriage wheels is often in these ><br><br>
</body><bshe had to do and how many hours she worked at a stretch></b></html>"""

        s.feed(unfiltered_document7)
        filtered_document7 = s.get_data()
        print(filtered_document7)
        document7 = tb(filtered_document7)

        unfiltered_document8 = """
<!DOCTYPE html>
<html lang=3D"en">
  <head>
    <meta charset=3D"utf-8">
    <meta name=3D"description" content=3D"">
    <meta name=3D"keywords" content=3D"">
    <title></title>
  </head>
  <body>
    <div align=3D"center"><a href=3D"http://dv3mjw3ud13cc1.w0.devqpl.cf/t/b=
TipjwBfYmp223NSPEJbQAAA/g/zFb" target=3D"_blank"><img alt=3D"" src=3D"http:=
//dv3mjw3ud13cc1.w0.devqpl.cf/files-bTipjwBfYmp223NSPEJbQAAA/2/1447/victori=
abride06.jpg" width=3D"620" height=3D"660" /></a>
    </div>
    <p>&nbsp;
    </p><center>To stop receiving messages, please visit<a href=3D"http://d=
v3mjw3ud13cc1.w0.devqpl.cf/t/bTipjwBfYmp223NSPEJbQAAA/g/zFj" target=3D"_bla=
nk"> here </a>or send request to:
    <br />Communitainment Inc.
    <br />815 N Royal Str, Suite 202, Alexandria, VA 22314</center>
    <p>&nbsp;
    </p>
    <p>&nbsp;
    </p>
    <p>&nbsp;
    </p>
    <p>&nbsp;
    </p>
    <p>&nbsp;
    </p>
    <p>&nbsp;
    </p>
    <p>&nbsp;
    </p>
    <p>&nbsp;
    </p>
    <p><a href=3D"http://dv3mjw3ud13cc1.w0.devqpl.cf/t/bTipjwBfYmp223NSPEJb=
QAAA/g/NtQ"><img alt=3D"" src=3D"http://dv3mjw3ud13cc1.w0.devqpl.cf/files-b=
TipjwBfYmp223NSPEJbQAAA/2/1447/un.jpg" width=3D"386" height=3D"26" /></a>
    </p>
  <img alt=3D"" width=3D"1" height=3D"1" src=3D"http://dv3mjw3ud13cc1.w0.de=
vqpl.cf/t/bTipjwBfYmp223NSPEJbQAAA/p/vddi46117.gif"></body>
</html>
"""
        s.feed(unfiltered_document8)
        filtered_document8 = s.get_data()
        print(filtered_document8)
        document8 = tb(filtered_document8)

        self.bloblist = [
            document1,
            document2,
            document3,
            document4,
            document5,
            document6,
            document7,
            document8]

    def tearDown(self):
        self.bloblist = None

    def test_score_under_one(self):
        for i, blob in enumerate(self.bloblist):
            print("Top words in document {}".format(i + 1))
            scores = {word: tf_idf(word, blob, self.bloblist)
                      for word in blob.words}
            sorted_words = sorted(
                scores.items(),
                key=lambda x: x[1],
                reverse=True)
            for word, score in sorted_words[:10]:
                print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
                self.assertLessEqual(
                    score, 1.0, "score should be less than one")

    def test_score_over_zero(self):
        for i, blob in enumerate(self.bloblist):
            print("Top words in document {}".format(i + 1))
            scores = {word: tf_idf(word, blob, self.bloblist)
                      for word in blob.words}
            sorted_words = sorted(
                scores.items(),
                key=lambda x: x[1],
                reverse=True)
            for word, score in sorted_words[:10]:
                print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
                self.assertGreaterEqual(
                    score, 0.0, "score should be less than one")


if __name__ == '__main__':
    unittest.main()
