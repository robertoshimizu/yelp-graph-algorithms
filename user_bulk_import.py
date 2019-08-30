import csv
import json
import os
import string
import random

#Check files and open dataset, set to append header and rows
if not os.path.isfile("data/user.csv"):
    with open("dataset/user.json") as user_json, \
            open("data/user.csv", 'a') as user_csv,\
		open("data/user_FRIEND_user.csv", 'a') as user_user_csv:

                # write headers
                csv.writer(user_csv).writerow(['user_id:ID', 'name', 'review_count', 'yelping_since', 'useful', 'funny', 'cool', 'fans', 'average_stars', 'compliment_hot', 'compliment_more', 'compliment_profile', 'compliment_cute', 'compliment_list', 'compliment_note', 'compliment_plain', 'compliment_cool', 'compliment_funny', 'compliment_writer', 'compliment_photos', ':LABEL'])

                # addition of id to enable identification of rel, weight as attribute to measure weight of rel
                csv.writer(user_user_csv).writerow([':START_ID', 'id', 'weight',':END_ID', ':TYPE'])

                # write rows
                count=1;

                for line in user_json.readlines():
                        item = json.loads(line)
                        csv.writer(user_csv).writerow([item["user_id"], item["name"], item["review_count"], item["yelping_since"], item["useful"], item["funny"], item["cool"], item["fans"], item["average_stars"], item["compliment_hot"], item["compliment_more"], item["compliment_profile"], item["compliment_cute"], item["compliment_list"], item["compliment_note"], item["compliment_plain"], item["compliment_cool"], item["compliment_funny"], item["compliment_writer"], item["compliment_photos"],"User"])

                        # format items["friends"], unwind them and then each one in a row
                        cara = item["friends"].replace(', ','')
                        friends = [cara[idx:idx+22] for idx,val in enumerate(cara) if idx%22 == 0]
                        for friend in friends:
                                # id will be a count+=1 and weight a random number between (1 - aquaintance/follower, 3- Friend/relative, 5 - close Friend/relative)
                                csv.writer(user_user_csv).writerow([item["user_id"], count,random.choice([1,3,5]) ,friend, "CONNECTED_TO"])
<<<<<<< HEAD
                                count+=1
=======
                                count+=1
                                

            

>>>>>>> 0bd97db22f67839a733c447c07879a2d5d6e3ac7
