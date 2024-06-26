vote_percentage_premise = 62.6
vote_percentage_hypothesis = 62.6

# the hypothesis mentions the vote percentage of Niinisto, which is also mentioned in the premise
if vote_percentage_hypothesis!= vote_percentage_premise:
    # check if the vote percentage in the hypothesis contradicts the vote percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
