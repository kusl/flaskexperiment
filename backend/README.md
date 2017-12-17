Can we make an effective spam filter using just term frequency and inverse document frequency?

Lets look at a few documents we came up with: 

Top words in document 1
	Word: Social, TF-IDF: 0.03772
	Word: social, TF-IDF: 0.03772
	Word: From, TF-IDF: 0.02368
	Word: records, TF-IDF: 0.01886
	Word: Kushal, TF-IDF: 0.01886
	Word: Ashamed, TF-IDF: 0.01886
	Word: Enter, TF-IDF: 0.01886
	Word: E-mail, TF-IDF: 0.01886
	Word: View, TF-IDF: 0.01886
	Word: Profiles, TF-IDF: 0.01886

This has the recipient's name in the top ten words. 
This is unfortunate because it is useless as a signal for an email being spam. 
It also does not work well across many people's inboxes. 
	
Top words in document 2
	Word: To, TF-IDF: 0.0364
	Word: score, TF-IDF: 0.0273
	Word: Kushal, TF-IDF: 0.02209
	Word: Your, TF-IDF: 0.02209
	Word: Dec, TF-IDF: 0.0182
	Word: 2017, TF-IDF: 0.0182
	Word: 16:14:54, TF-IDF: 0.0182
	Word: 0600, TF-IDF: 0.0182
	Word: Ashamed, TF-IDF: 0.01473
	Word: Social, TF-IDF: 0.01473
	
Again, the recipient's name is in the top ten words. 	
	
Top words in document 3
	Word: To, TF-IDF: 0.03699
	Word: Kushal, TF-IDF: 0.01995
	Word: Click, TF-IDF: 0.01995
	Word: score, TF-IDF: 0.01849
	Word: Is, TF-IDF: 0.01521
	Word: Ashamed, TF-IDF: 0.01496
	Word: unsubscribe, TF-IDF: 0.01496
	Word: DailyDeal, TF-IDF: 0.01496
	Word: LLC, TF-IDF: 0.01496
	Word: 11923, TF-IDF: 0.01496
	
Again, the recipient's name is in the top ten words. 

Top words in document 4
	Word: To, TF-IDF: 0.03916
	Word: Kushal, TF-IDF: 0.02218
	Word: Click, TF-IDF: 0.02218
	Word: City, TF-IDF: 0.01803
	Word: Ashamed, TF-IDF: 0.01584
	Word: city, TF-IDF: 0.01449
	Word: unsubscribe, TF-IDF: 0.01268
	Word: DailyDeal, TF-IDF: 0.01268
	Word: LLC, TF-IDF: 0.01268
	Word: 11923, TF-IDF: 0.01268
	
Again, the recipient's name is in the top ten words. 	
	
Top words in document 5
	Word: To, TF-IDF: 0.04311
	Word: Kushal, TF-IDF: 0.02035
	Word: Click, TF-IDF: 0.02035
	Word: City, TF-IDF: 0.01654
	Word: Ashamed, TF-IDF: 0.01453
	Word: city, TF-IDF: 0.01329
	Word: unsubscribe, TF-IDF: 0.01163
	Word: DailyDeal, TF-IDF: 0.01163
	Word: LLC, TF-IDF: 0.01163
	Word: 11923, TF-IDF: 0.01163	
	
Again, the recipient's name is in the top ten words. 

Top words in document 6
	Word: OF, TF-IDF: 0.0865
	Word: The, TF-IDF: 0.0343
	Word: CONGO, TF-IDF: 0.02768
	Word: Congo, TF-IDF: 0.02768
	Word: KABILA, TF-IDF: 0.02768
	Word: Kabila, TF-IDF: 0.02768
	Word: the, TF-IDF: 0.02746
	Word: YOUR, TF-IDF: 0.0271
	Word: In, TF-IDF: 0.02439
	Word: WE, TF-IDF: 0.02076	
	
This one looks a bit better but common words like of, the, your, in, we get caught up. 
I assume we don't want that. 

Top words in document 7
	Word: My, TF-IDF: 0.03746
	Word: As, TF-IDF: 0.03173
	Word: The, TF-IDF: 0.0213
	Word: Now, TF-IDF: 0.01983
	Word: my, TF-IDF: 0.01967
	Word: the, TF-IDF: 0.01705
	Word: I, TF-IDF: 0.01612
	Word: charity, TF-IDF: 0.01586
	Word: life, TF-IDF: 0.0119
	Word: less, TF-IDF: 0.0119
	
This is pretty much useless. 	
	
Top words in document 8
	Word: i, TF-IDF: 0.05942
	Word: the, TF-IDF: 0.03275
	Word: client, TF-IDF: 0.01981
	Word: US, TF-IDF: 0.01552
	Word: Agabi, TF-IDF: 0.01486
	Word: agabi, TF-IDF: 0.01486
	Word: All, TF-IDF: 0.01486
	Word: Since, TF-IDF: 0.01486
	Word: next, TF-IDF: 0.01486
	Word: Mr, TF-IDF: 0.01164
	
This looks a bit more helpful but how can we tell?

Top words in document 9
	Word: AND, TF-IDF: 0.07603
	Word: The, TF-IDF: 0.04038
	Word: the, TF-IDF: 0.03233
	Word: YOUR, TF-IDF: 0.02836
	Word: Abacha, TF-IDF: 0.01448
	Word: Security, TF-IDF: 0.01418
	Word: You, TF-IDF: 0.01209
	Word: security, TF-IDF: 0.0114
	Word: Mohammed, TF-IDF: 0.01086
	Word: Also, TF-IDF: 0.01086
	
This is pretty much useless. 	
	
Top words in document 10
	Word: Of, TF-IDF: 0.04821
	Word: The, TF-IDF: 0.03866
	Word: the, TF-IDF: 0.03095
	Word: Us, TF-IDF: 0.02552
	Word: interested, TF-IDF: 0.01702
	Word: Account, TF-IDF: 0.01702
	Word: This, TF-IDF: 0.01523
	Word: MY, TF-IDF: 0.01333
	Word: us, TF-IDF: 0.01303
	Word: would, TF-IDF: 0.0125

This is also useless. 
	
Top words in document 11
	Word: ayy, TF-IDF: 0.9359
	Word: lmao, TF-IDF: 0.9359
	
This was a test string with just two words "ayy" and "lmao". 
Of course, these are the top two words because they are the only words. 
	
Top words in document 12
	Word: drcep, TF-IDF: 0.02753
	Word: nioahnqw, TF-IDF: 0.02753
	Word: narxbd, TF-IDF: 0.02753
	Word: wgd, TF-IDF: 0.02753
	Word: ysmiu, TF-IDF: 0.02753
	Word: hbplfufm, TF-IDF: 0.02753
	Word: gabldc, TF-IDF: 0.02753
	Word: mip, TF-IDF: 0.02753
	Word: ipzzf, TF-IDF: 0.02753
	Word: mtpgkour, TF-IDF: 0.02753
	
This is gibberish to see what happens. 	
	
Top words in document 13
	Word: IN, TF-IDF: 0.04505
	Word: In, TF-IDF: 0.03529
	Word: The, TF-IDF: 0.03215
	Word: the, TF-IDF: 0.02574
	Word: Your, TF-IDF: 0.02538
	Word: World, TF-IDF: 0.02458
	Word: WORLD, TF-IDF: 0.02458
	Word: BANK, TF-IDF: 0.02458
	Word: UNITED, TF-IDF: 0.02048
	Word: Contact, TF-IDF: 0.02048
	
This also has the problem of catching up two different forms of IN and In as well as The and the. 

What are we doing wrong? 
How can we fix it? 
