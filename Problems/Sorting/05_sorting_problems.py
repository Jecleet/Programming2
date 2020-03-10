'''
Sorting and Intro to Big Data Problems (22pts)

Import the data from NBAStats.py.  The data is all in a single list called 'data'.
I pulled this data from the csv in the same folder and converted it into a list for you already.
For all answers, show your work
Use combinations of sorting, list comprehensions, filtering or other techniques to get the answers.
'''

def split_line(line):
    # This function takes in a line of text and returns
    # a list of words in the line.
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

from NBAStats import data


#1  Pop off the first item in the list and print it.  It contains the column headers. (1pt)
print(data.pop(0))

#2  Print the names of the top ten highest scoring single seasons in NBA history?
# You should use the PTS (points) column to sort the data. (4pts)

pts_list = []
data_point = data[2]
length = len(data_point) - 1
for i in range(len(data)):
    pts_list.append(data[i][length])
    print#  Why doesn't this work??
pts_list2 = pts_list[:]
print (pts_list2)
for i in range(10):
    max_value = max(pts_list) # finds the max of the list
    max_value_index = pts_list.index(max_value) # finds the place in the list where this value occurs
    pts_list.pop(max_value_index)  # removes this from pts_list so that next time it will find the next biggest number
    max_value_index = pts_list2.index(max_value)  # checks a list which has not had anything popped off so the numbers still align with the names
    print(data[max_value_index][2]) #uses the index from the list which doesn't have values popped off to find the name corresponding with each number??

#3  How many career points did Kobe Bryant have? Add up all of his seasons. (4pts)
name = ''
goal_name = "Kobe Bryant"
career_points = 0
done = False
for i in range(len(data)):
    name = data[i][2]
    if name.upper() == goal_name.upper():
        length = len(data[i]) - 1
        career_points += data[i][length]
print(career_points)
#4  What player has the most 3point field goals in a single season. (3pts)

points_list = []
for i in range(len(data)):
    points_list.append(data[i][-19])
index = points_list.index(max(points_list))
print(data[index][2])

#5  One stat featured in this data set is Win Shares(WS). -28
#  WS attempts to divvy up credit for team success to the individuals on the team.
#  WS/48 is also in this data.  It measures win shares per 48 minutes (WS per game).
#  Who has the highest WS/48 season of all time? (4pts)

win_shares_list = []
for i in range(len(data)):
    win_shares_list.append(data[i][-28])
index = win_shares_list.index(max(win_shares_list))
print(data[index][2])

#6  Write your own question that you have about the data and provide an answer (4pts)
# Maybe something like: "Who is the oldest player of all time?"  or "Who played the most games?"  or "Who has the most combined blocks and steals?".
# Who is the oldest player of all time?
age_list = []
for i in range(len(data)):
    age_list.append(data[i][4])
index = age_list.index(max(age_list))
print(data[index][2])

#7  Big challenge, few points.  Of the 100 highest scoring single seasons in NBA history, which player has the
# worst free throw percentage?  Which had the best? (2pts)
most_pts = 0
current_pts = 0
player = ''
list_100_players_points = []
list_100_players = []
data2 = data[:]
for m in range(100):
    for i in range(len(data2)):
        current_pts = data2[i][-1]
        if current_pts > most_pts:
            most_pts = current_pts
            player = data2[i][2]
            player_place = i
    list_100_players.append(data2[player_place][2])
    list_100_players_points.append(data2[player_place][-1])
    data2.pop(player_place)
index = int(min(list_100_players_points))
print(list_100_players[index])






