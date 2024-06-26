people_premise = 20
people_hypothesis = 60
visited_iceland_premise = 35
visited_iceland_hypothesis = 35
visited_norway_premise = 23
visited_norway_hypothesis = 23

# the hypothesis refers to the number of people and the number of people who have visited Iceland and Norway, which are also mentioned in the premise
if people_hypothesis < people_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
elif visited_iceland_hypothesis!= visited_iceland_premise:
    # check if the number of people who visited Iceland in the hypothesis contradicts the number of people who visited Iceland reported in the premise
    label = "contradiction"
elif visited_norway_hypothesis!= visited_norway_premise:
    # check if the number of people who visited Norway in the hypothesis contradicts the number of people who visited Norway reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
