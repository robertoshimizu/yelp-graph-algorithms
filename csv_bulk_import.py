import csv
import json
import os
import string
import random

#Check files and open dataset, set to append header and rows
"""
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
                                    count+=1

"""
if not os.path.isfile("data/review_node.csv"):
    with open("dataset/review.json") as review_json, \
            open("data/review.csv", 'a') as review_csv, \
                open("data/user_review.csv", 'a') as user_review_csv, \
                    open("data/review_business.csv", 'a') as review_business_csv:

                        csv.writer(review_csv).writerow(['review_id:ID(Review-ID)', 'stars', 'date', 'text', 'useful', 'funny', 'cool', ':LABEL'])
                        csv.writer(user_review_csv).writerow([':START_ID(User-ID)',':END_ID(Review-ID)', ':TYPE'])
                        csv.writer(review_business_csv).writerow([':START_ID(Review-ID)',':END_ID(Business-ID)', ':TYPE'])

                        for line in review_json.readlines():
                            item = json.loads(line)
                            csv.writer(review_csv).writerow([item["review_id"], item["stars"], item["date"],item["text"], item["useful"], item["funny"], item["cool"], "Review"])
                            csv.writer(user_review_csv).writerow([item["user_id"], item["review_id"], "WROTE"])
                            csv.writer(review_business_csv).writerow([item["review_id"], item["business_id"], "REVIEWS"])

if not os.path.isfile("data/business.csv"):
    with open("dataset/business.json") as business_json, \
            open("data/business.csv", 'a') as business_csv:

                csv.writer(business_csv).writerow(['business_id:ID(Business-ID)', 'name', 'address', 'city', 'state','postal_code', 'latitude', 'longitude', 'stars', 'review_count', 'is_open', 'attributes', 'categories', ':LABEL'])
                business_writer = csv.writer(business_csv)
                for line in business_json.readlines():
                    item = json.loads(line)
                    business_writer.writerow(
                            [item["business_id"], item["name"], item["address"], item["city"], item["state"],
                            item["postal_code"], item["latitude"], item["longitude"], item["stars"], item["review_count"], item["is_open"], item["attributes"], item["categories"], "Business"])


if not os.path.isfile("data/category.csv"):
    with open("dataset/business.json") as business_json, \
            open("data/category.csv", 'a') as categories_csv, \
                open("data/business_in_category.csv", 'a') as business_category_csv:

                    csv.writer(categories_csv).writerow(['category_id:ID(Category-ID)', 'name', ':LABEL'])
                    csv.writer(business_category_csv).writerow([':START_ID(Business-ID)',':END_ID(Category-ID)', ':TYPE'])

                    unique_categories = []
                    for line in business_json.readlines():
                        item = json.loads(line)
                        if item["categories"]:
                            categories = list(item["categories"].split(", "))
                            for category in categories:                                    
                                    if category not in unique_categories:
                                            unique_categories.append(category)
                                            category_id = unique_categories.index(category)
                                            csv.writer(categories_csv).writerow([category_id, category, "Category"])
                                    else:
                                        category_id = unique_categories.index(category)
                                        csv.writer(business_category_csv).writerow([item["business_id"], category_id, "IN_CATEGORY"])

if not os.path.isfile("data/city.csv"):
    with open("dataset/business.json") as business_json, \
            open("data/city.csv", 'a') as city_csv, \
                open("data/state.csv", 'a') as state_csv, \
                    open("data/business_city.csv", 'a') as business_city_csv, \
                        open("data/city_state.csv", 'a') as city_state_csv:

                            csv.writer(city_csv).writerow(['city_id:ID(City-ID)', 'city', ':LABEL'])
                            csv.writer(business_city_csv).writerow([':START_ID(Business-ID)',':END_ID(City-ID)', ':TYPE'])
                            csv.writer(state_csv).writerow(['state_id:ID(State-ID)', 'state', ':LABEL'])
                            csv.writer(city_state_csv).writerow([':START_ID(City-ID)',':END_ID(State-ID)', ':TYPE'])

                            unique_cities = []
                            unique_states = []
                            unique_city_state = []
                            unique_business_city = []
                            for line in business_json.readlines():
                                item = json.loads(line)
                                if item["city"]:
                                        if item["city"] not in unique_cities:
                                            unique_cities.append(item["city"])
                                            city_id = unique_cities.index(item["city"])
                                            csv.writer(city_csv).writerow([city_id, item["city"], "City"])
                                        else:
                                            city_id = unique_cities.index(item["city"])
                                            if unique_business_city==[]:
                                                csv.writer(business_city_csv).writerow([item["business_id"], city_id, "IN_CITY"])
                                                unique_business_city.append((item["business_id"],city_id))
                                                #print((city_id, state_id))
                                            else:
                                                if ((item["business_id"],city_id)) not in unique_business_city:
                                                    unique_business_city.append((item["business_id"],city_id))
                                                    csv.writer(business_city_csv).writerow([item["business_id"], city_id, "IN_CITY"])
                                                    #print((city_id, state_id))                                       
                                if item["state"]:
                                        if item["state"] not in unique_states:
                                            unique_states.append(item["state"])
                                            state_id = unique_states.index(item["state"])
                                            csv.writer(state_csv).writerow([state_id, item["state"], "Area"])
                                        else:
                                            state_id = unique_states.index(item["state"])
                                            if item["city"]:
                                                city_id = unique_cities.index(item["city"])
                                            else:
                                                city_id = len(unique_cities) + 1
                                if unique_city_state==[]:
                                    csv.writer(city_state_csv).writerow([city_id, state_id, "IN_AREA"])
                                    unique_city_state.append((city_id, state_id))
                                    #print((city_id, state_id))
                                else:
                                    if ((city_id,state_id)) not in unique_city_state:
                                        unique_city_state.append((city_id, state_id))
                                        csv.writer(city_state_csv).writerow([city_id, state_id, "IN_AREA"])
                                        #print((city_id, state_id))
                    
