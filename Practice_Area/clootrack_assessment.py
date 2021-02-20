"""
Assignment: Find who tweeted the most

You will be given a list of tweets
Your program should find the user who has tweeted the most

Note:
If multiple users are having same number of tweets, then print all the users in alphabetical order of user names.
Use Python 3
Follow python coding style guide
Only <filename>.py file should be uploaded. Do not upload <filename>.ipnb file

Input format:
Read the input from console.
First line of input should be number of test cases
Remaining lines of input should contain each test case input.

For each test case input:
First line should contain number of tweets.
Followed by N lines, each containing user name and tweet id separated by a space.

Output format:
Find the user with max number of tweets. Print user name and total number of tweets.

Sample 1:
Input
1
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sachin tweet_id_4

Output
sachin 3

"""


def max_tweet(arr):
    temp_dict = {}
    max_tweet_list = ''
    for k in arr:
        temp = k.split()
        if temp_dict.get(temp[0]):
            temp_dict[temp[0]] += 1
        else:
            temp_dict[temp[0]] = 1
    max_count = list(temp_dict.values()).count(max(temp_dict.values()))
    if max_count == 1:
        max_key = max(temp_dict, key=lambda l: temp_dict[l])
        max_tweet_list = str(max_key) + ' ' + str(temp_dict[max_key])
    else:
        for x in range(max_count):
            max_key = max(temp_dict, key=lambda l: temp_dict[l])
            max_tweet_list += str(max_key) + ' ' + str(temp_dict[max_key]) + ','
            temp_dict.pop(max_key)

    return max_tweet_list.strip(',')


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        arr_tweets = []
        total_tweets = int(input())
        for j in range(total_tweets):
            arr_tweets.append(input().strip())
        for l in max_tweet(arr_tweets).split(','):
            print(l)
