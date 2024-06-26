people_premise = 60
people_hypothesis = 40
iceland_visited_premise = 35
iceland_visited_hypothesis = 35
norway_visited_premise = 23
norway_visited_hypothesis = 23

# the hypothesis talks about the number of people and the number of people who have visited Iceland and Norway, referenced also in the premise
if people_hypothesis!= people_premise:
    # check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
elif iceland_visited_hypothesis!= iceland_visited_premise:
    # check if the number of people who have visited Iceland in the hypothesis contradicts the number of people who have visited Iceland reported in the premise
    label = "contradiction"
elif norway_visited_hypothesis!= norway_visited_premise:
    # check if the number of people who have visited Norway in the hypothesis contradicts the number of people who have visited Norway reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
