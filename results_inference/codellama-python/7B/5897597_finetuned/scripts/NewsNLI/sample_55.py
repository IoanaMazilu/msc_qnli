semifinals_premise = 2
semifinals_hypothesis = 2
final_premise = 1
final_hypothesis = 1

# the hypothesis mentions the number of national semifinal games and the final, which are also mentioned in the premise
if semifinals_hypothesis!= semifinals_premise:
    # check if the number of semifinal games in the hypothesis contradicts the number of semifinal games reported in the premise
    label = "contradiction"
elif final_hypothesis!= final_premise:
    # check if the number of final games from the hypothesis contradicts the number of final games in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
