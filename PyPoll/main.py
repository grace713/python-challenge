import csv

with open('election_data.csv') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    dataList = list(data)

sumOfVotes = 0
candidates = {}
dataList.pop(0)

for entry in dataList:
    candidate = entry[2]
    sumOfVotes = sumOfVotes + 1
    if not (candidates.has_key(candidate)):
        candidates[candidate] = 0
    else:
        candidates[candidate] = candidates[candidate] + 1

winner = max(candidates.iterkeys(), key=(lambda key: candidates[key]))

# for candidate in candidates:
#     if candidate[1] > winner[1]:
#         winner = candidate
work = {}
for candidate in candidates:
    work[candidate] = round(float(candidates[candidate])/sumOfVotes*100)

print("Election Results")
print("-------------------------")
print("Total Votes: "+ str(sumOfVotes))
print("-------------------------")
while(len(work) != 0):
    candidate = max(work.iterkeys(), key=(lambda key: work[key]))
    print(candidate + ": " + str(round(float(candidates[candidate]) / sumOfVotes * 100)) + "% (" + str(candidates[candidate]) + ")")
    work.pop(candidate)
print("-------------------------")
print("Winner: "+winner)
print("-------------------------")
