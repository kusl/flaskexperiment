import unittest

from textblob import TextBlob as tb

from my_message.TfIdf import tf_idf


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
        self.bloblist = [document1, document2, document3]

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
