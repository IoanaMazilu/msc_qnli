total_people_premise = 60
visited_iceland_premise = 35
visited_norway_premise = 23
total_people_hypothesis = 40
visited_iceland_hypothesis = 35
visited_norway_hypothesis = 23

# the hypothesis talks about the number of people who visited Iceland and Norway, referenced also in the premise
if visited_iceland_hypothesis!= visited_iceland_premise:
    # check if the number of people who visited Iceland in the hypothesis contradicts the number of people who visited Iceland in the premise
    label = "contradiction"
elif visited_norway_hypothesis!= visited_norway_premise:
    # check if the number of people who visited Norway in the hypothesis contradicts the number of people who visited Norway in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
