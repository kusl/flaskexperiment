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
        document8 = tb(filtered_document8)

        # few from http://www.hoax-slayer.com/nigerian-scam-examples.html

        document9 = tb(
            """FROM: MR DAN PATRICK. DEMOCRATIC REPUBLIC OF CONGO. ALTERNATIVE EMAIL: (patrickdan@rediffmail.com). Dear Sir, SEEKING YOUR IMMEDIATE ASSISTANCE. Please permit me to make your acquaintance in so informal a manner. This is necessitated by my urgent need to reach a dependable and trust wordy foreign partner. This request may seem strange and unsolicited but I will crave your indulgence and pray that you view it seriously. My name is. DAN PATRICK of the Democratic Republic of Congo and One of the close aides to the former President of the Democratic Republic of Congo LAURENT KABILA of blessed memory, may his soul rest in peace. Due to the military campaign of LAURENT KABILA to force out the rebels in my country, I and some of my colleagues were instructed by Late President Kabila to go abroad to purchase arms and ammunition worth of Twenty Million, Five Hundred Thousand United States Dollars only (US$20,500,000.00) to fight the rebel group. But when President Kabila was killed in a bloody shoot-out by one of his aide a day before we were schedule to travel out of Congo, We immediately decided to divert the fund into a private security company here in Congo for safe keeping. The security of the said amount is presently being threatened here following the arrest and seizure of properties of Col.Rasheidi Karesava (One of the aides to Laurent Kabila) a tribesman, and some other Military Personnel from our same tribe, by the new President of the Democratic Republic of Congo, the son of late President Laurent Kabila, Joseph Kabila. In view of this, we need a reliable and trustworthy foreign partner who can assist us to move this money out of my country as the beneficiary. WE have sufficient ''CONTACTS'' to move the fund under Diplomatic Cover to a security company in the Europe in your name. This is to ensure that the Diplomatic Baggage is marked ''CONFIDENTIAL'' and it will not pass through normal custom/airport screening and clearance. Our inability to move this money out of Congo all This while lies on our lack of trust on our supposed good friends (western countries) who suddenly became hostile to those of us who worked with the late President Kabila, immediately after his son took office. Though we have neither seen nor met each other, the information we gathered from an associate who has worked in your country has encouraged and convinced us that with your sincere assistance, this transaction will be properly handled with modesty and honesty to a huge success within two weeks. The said money is a state fund and therefore requires a total confidentiality. Thus, if you are willing to assist us move this fund out of Congo, you can contact me through my email address above with your telephone, fax number and personal information to enable us discuss the modalities and what will be your share (percentage) for assisting us. I must use this opportunity and medium to implore You to exercise the utmost indulgence to keep this Matter extraordinarily confidential, Whatever your Decision, while I await your prompt response. NOTE: FOR CONFIDENTIALITY, I WILL ADVISE YOU REPLY ME ON MY ALTERNATIVE EMAIL BOX (patrickdan@rediffmail.com).Thank you and God Bless. Best Regards, MR DAN PATRICK.""")

        document10 = tb("""Dear Friend.

As you read this, I don't want you to feel sorry for me, because, I believe everyone will die someday.

My name is Peter Lawson,a merchant in Dubai, in the U.A.E.I have been diagnosed with Esophageal Cancer which was discovered very late,due to my laxity in carrying for my health. It has defiled all forms of medicine, and right now I have only about a few months to live, according to medical experts.

I have not particularly lived my life so well, as I never really cared for anyone not even myself but my business. Though I am very rich, I was never generous, I was always hostile to people and only focus on my business as that was the only thing I cared for. But now I regret all this as I now know that there is more to life than just wanting to have or make all the money in the world. I believe when God gives me a second chance to come to this world I would live my life a different way from how I have lived it.

Now that God ! has called me, I have willed and given most of my properties and assets to my immediate and extended family members and as well as a few close friends. I want God to be merciful to me and accept my soul and so, I have decided to give arms to charity organizations and give succour and confort to the less priviledged in our societies, as I want this to be one of the last good deeds I do on earth.

So far, I have distributed money to some charity organizations in the U.A.E, Algeria and Malaysia. Now that my health has deteriorated so badly, I cannot do this my self anymore. I once asked members of my family to close one of my accounts and distribute the money which I have there to charity organization and to the less priviledged in Bulgaria and Pakistan, they refused and kept the money to themselves. Hence, I do not trust them anymore, as they seem not to be contended with what I have left for them.

The last of my money which no one knows of is the huge cash deposit of twenty four million dollars that I have with a Security Company in Europe for safe keeping. I will want you to help me collect this deposit and disburse it to some charity organizations and to the less priviledged.

Please send me a mail to indicate if you will assist me in this disbursement.

I have set aside 10% for you for your time and patience.

You can e-mail me at:plawson@hknetmail.com

While I await to hear from you, may God be with you and your entire family.

Remain blessed.

Mr.Peter Lawson""")
        document11 = tb("""Agabi and Associates.
Solicitors and Advocates.
5th floor, Unity House.
Lagos.

Dear (recipaints name),

I am Mr. paul agabi, a Lawyer by profession. I am the personal attorney to Mr. Charles (my surname) , a national of your country, who used to work with Chevron Oil Exploration Company in Nigeria, herein after shall be referred to as my client.

On the 21st of April 2000, my client, his wife and their onlye child were involved in a car accident along Lagos - Ibadan express road. All occupants of the vehicle unfortunately lost there lives.

Since then I have made several enquiries to your embassy to locate any of my clients extended relatives. This has proved unsuccessful. I came to know about you through an enquiry I was making in the internet, and I found out you shared the same surname with my client, which is why I have decided to contact you, in order to assist in repatriating the money and property left behind by my client before they get confiscated or declared unserviceable by the bank.

Particularly, in a local commercial bank here where the deceased had an account valued at about US$ 15.5 Million Dollars, has issued me a notice to provide the next of kin or have the account confisticated within the next ten official working days.

Since i have been unsuccessful in locating the relatives for over 2 years now I seek your consent to present you as the next of kin of the deceased since you have the same last name so that the proceeds of this account valued at US$15.5 Million Dollars can be paid to you and then you and me can share the money, on the ratio of 50% for me, and 50% for you.

I have all necessary legal documents that can be used to back up any claim we may make. All I require is your honest co-operation to enable us see this business through. I guarantee that this will be executed under a legitimate arrangement that will protect you from any breach of the law.

Please get in touch with me by email and send to me your telephone and fax numbers to enable us discuss further about the details of this transaction.

Best regards, Mr. paul agabi.""")
        document12 = tb("""From:Mohammed Abacha Lagos-Nigeria Tel: 234-80-34069502

Dear Sir/Madam

This letter is not intended to to cause any embarrassment but just to contact your esteem self-following the knowledge of your high repute and trustworthiness.

I am Mohammed Abacha,the son of the late Nigerian Head of State who died on the 8th of June 1998.If you are conversant with world news,you would understand better,while I got your contacts through my personal research.Please,I need your assistance to make this happen and please; do not undermine it because it will also be a source of upliftment to you also.You have absolutely nothing to loose in assisting us instead, you have so much to gain.

The then head of state General Sani Abacha,transferred the money through a Lebanese businessman,Chagoury and a Jewish business man,Mark Rissar to bank accounts overseas,Instead,he used PERSONAL IDENTIFICATION NUMBERS (PIN) and declared the contents as Bearer Bonds and Treasury Bills. Also the firm issued him with a certificate of deposit of the consignments notes, which I have these information in my custody now.

You must have heard over the media reports and the Internet on the recovery of various huge sums of money deposited by my late father in different Banks and security firms abroad. Some of these banks and security firms willingly gave-/divulge their banking secrets and disclosed to the present civilian administration of Chief Olusegun Obasanjo,about my family's cash lodgement and monetary transactions with them.

Please my dear,I repose great confidence in you and I hope you will not betray my confidence in you.I have secretly deposited the sum of $30,000,000.00 with a security firm abroad whose name is withheld for now until we open communications.The money is contained in a metal box consignment with Security Deposit Number 009GM.

I shall be grateful if you could receive this fund into your Bank account for safekeeping. This arrangement is known to you and my junior brother (Abbas) only. So I will deal directly with you.I am proposing a 20% share of the fund to you for your kind assistance.I shall provide for you all the documents of the fund deposit with the security firm, and raise a power of attorney to enable you claim and receive this fund into your bank account.I have done a thorough homework and fine-tuned the best way to create you as the beneficiary to the funds and effect the transfer accordingly.Is rest assured that the modalities I have resolved to finalize the entire project guarantees our safety and the successful transfer of the funds.So, you will be absolutely right when you say that this project is risk free and viable.If you are capable and willing to assist, contact me at once via email with following details:

1. YOUR NAME
2. POSTAL ADDRESS
3. PHONE AND FAX NUMBERS

Also this transaction demands absolute confidentiality.On no condition must you disclose it to anybody irrespective of your relation with the person.Remember,Loose lips sinks ship.I am looking forward to your urgent and positive response via my email address above.

Best Regards,

Mohammed Abacha.""")
        document13 = tb("""From: Dr.Goronyo Baba.

Satellite Tel: Note:Do not send emails.You can contact me directly on the tel.number or by sending me a satellite message stating your telephone number and email address contact on this number just given to you using the link online below. http://www.iridium.com/..there, you will see send a satellite message to my sat.tel.number- 881-631-410-574

Attn:President/C.e.o.

Strictly Confidential and Urgent Business Proposal.

Re: Transfer Of Usd $21,500.000{Twenty - One Million, Five Hundred Thousand Us Dollars Only.

I am a member of the Federal Government Of Nigerian National Petroleum Corporation (N.N.P.C). Sometime ago, a contract was awarded to a foreign firm in the Petroleum Trust Fund (P.T.F.) BY MY COMMITTEE.

This contract was over invoiced to the tune of us$ 21.5Million Dollars. This was done delibrately. The over - invoicing was a deal by my committee to benefit from the project. We not want to transfer this money, which is in a suspense account with the P.T.F. into any oversea account, which we expect you to provide for us.

Share:
60 % of the money would be for my partners and I. 30 % of the money would be yours, for providing us with logistics, which, would include a safe bank account, where we shall facilitate funds transfer into, as soon as documentations are concluded over here. 10 % of the money has been mapped out from the total sum to cover any expenses that might be incurred during the course of the transaction, (both local and international expenses).

If interested in assisting us, please contact me via my secured satellite tel number- 881-631-410-574, specially procured for this project, using the text message..

It may interest you to know that a similar transaction was carried out with one Mr. Patrice Miller, President of Crane International Trading Corp., of 153 East 57th St., 28th floor, N.Y.10022, Telephone: 212-308-7788 and Telex: 6731689. The deal was concluded and all covering documents, forwarded to Mr. Miller to authenticate the claims. Once the funds were transferred, Mr. Miller presented to his bank, all the legal documents and remitted the whole funds to another bank account, and disappeared completely. My colleagues and I were shattered, since such opportunities are not easy to come by.

Please, if you are interested in assisting us carry out to the fullest capacity, this transaction, we would require the following information from you which would enable us make formal application to the various ministries / parastatals, for the release and onward transfer of the money to your account.

1.Your Full Name, Company's Name, Address, Telephone and Fax Numbers. 2.Your Bank Name, Address. Telephone and Fax Number. 3.Your Bank Account Number and Beneficiary Name - You must be the signatory.

Please, note that we have strong and reliable connections at the Central Bank Of Nigeria and other Government Parastatals, hence assistance in this regards, would not be a problem. At the conclusion of this transaction, we shall use same contacts to withdraw all documents used in the course of this, to avoid any trace whatsoever that may ever arise, to you or to us, now and in the nearest possible future.

It might also interest you to know that we are mere civil servants who do not want to miss this opportunity, hence, we want this money transferred out, as soon as possible, before the newly democratically elected government ever think of making enquiries as regards the various activities of the past military government.

Kindly contact me as soon as possible, whether or not you are interested in this deal, so that whereby you are not interested, it would give us more room to scout for another partner. But if you are interested, kindly contact me via above email, telephone or fax, so that we can swing into action, as time is not on our part.

I wait in anticipation of your fullest co-operation. Yours Faithfully,


Dr.Goronyo Baba.

Send me your email address and tel.numberif interested for re- verification that you actually received this mail. """)

        document14 = tb("""ayy lmao""")
        document15 = tb(
            """drcep nioahnqw narxbd wgd. ysmiu hbplfufm gabldc mip. ipzzf mtpgkour ccdszv xky. adqvu yajkmifx bwcsba aba. klklf yuhuswln ihmymt ufy. cqctb hwjexlim opmvfl arm. hloiw wjzahuiv ksypfa yfm. uqqpz txixfekk ferstv mkf. uszvv pldrxjsy thzzji axy. mehlj kfmzeyra gggyeo srl. qmrgq onqtqtjh psnpzd nau. jfhmk etfxcjfd ryvydq htg. spiki upoiitsy rckroh dxs. pruki qsbcrait kbbuvb lwl. pebef ybnpakwq szmoax mle. kdhvh bbwzgnkj hlewid fgq. jnvjl ahjncwtz olnvvj cie.""")
        document16 = tb(
            """The United Nations Headquarters United Nations Compensation Unit In Affiliation with World Bank Our Ref: U.N/WBO/042UK/2016 New York
Congratulations Beneficiary
[1]United Nation goal to eradicate global poverty before 2020.
[2]Financial support to individuals, family and organization with bright purpose to fund their project.
[3]World/community development.
[4]Your email was submitted by the all world email providers and was chosen by ballot. [5]The beneficiary will sponsor the claim charge of their cheque.
We have been having a meeting for the past 7 months which just ended few days ago with the secretary to the UNITED NATIONS. This email is to all the people that have been scammed in any part of the world and families,individuals,organizations that needs financial support, the UNITED NATIONS in Affiliation with WORLD BANK have agreed to compensate them with the sum of USD$5 Million Dollars.
This includes every foreign contractors that may have not received their contract sum, and people that have had an unfinished transaction or international businesses that failed due to Government problems etc. We found your name in the list of those who are to benefit from these compensation exercise and that is why we are contacting you, this have been agreed upon and have been signed. You are advised to contact Aaron Smith of our paying center in Africa, as he is our representative in Nigeria, contact him immediately for your Cheque/ International Bank Draft of USD$5 Million Dollars.
This fund is in form of a Bank Draft for security purpose ok? So he will send it to you and you can clear it in any bank of your choice. Therefore, you should send him your full Name and telephone number your correct mailing address where you want him to send the Draft to you. Contact Aaron Smith of MAGNUM PLC PAYMENT CENTER with your payment Code:ST/DPI/829 immediately for your Cheque at the given address below:
DIRECTOR IN CHARGE: Aaron Smith E-MAIL: cbn-atmclaimdept@gmx.com

TELEPHONE+2348105744165 FAX: +234-1-8968850
I apologize on behalf of my organization for any delay you might have encountered in receiving your fund in the past. Thanks and God bless you and your family. Hoping to hear from you as soon as you cash your Bank Draft. Making the world a better place.
You are required to contact the above person and furnish him with the following of your information that will be required to avoid any mistakes:-
1. Your Full name:
2. Your Country:
3. Contact Address: 4. Telephone Number: 5. Fax Number:
6. Marital Status:
7. Occupation:
8. Sex:
9. Age:
Congratulations, and I look forward to hear from you as soon as you confirm your payment making the world a better place.
Regards,
Secretary-General Ban Ki-Moon""")
        
        self.blob_list = [
            document4,
            document5,
            document6,
            document7,
            document8,
            document9,
            document10,
            document11,
            document12,
            document13,
            document14,
            document15,
            document16,
        ]

    def tearDown(self):
        self.blob_list = None

    def test_score_under_one(self):
        for i, blob in enumerate(self.blob_list):
            print("Top words in document {}".format(i + 1))
            scores = {word: tf_idf(word, blob, self.blob_list)
                      for word in blob.words}
            sorted_words = sorted(
                scores.items(),
                key=lambda x: x[1],
                reverse=True)
            for word, score in sorted_words[:10]:
                print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
                self.assertLessEqual(
                    score, 1.0, "score should be less than one")

    def test_score_over_negative_one(self):
        for i, blob in enumerate(self.blob_list):
            print("Top words in document {}".format(i + 1))
            scores = {word: tf_idf(word, blob, self.blob_list)
                      for word in blob.words}
            sorted_words = sorted(
                scores.items(),
                key=lambda x: x[1],
                reverse=True)
            for word, score in sorted_words[:10]:
                print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
                self.assertGreaterEqual(
                    score, -1.0, "score should be less than one")


if __name__ == '__main__':
    unittest.main()
