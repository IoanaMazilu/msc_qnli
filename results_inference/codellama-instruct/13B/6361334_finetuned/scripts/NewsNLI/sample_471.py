goals_premise = 5
goals_hypothesis = 5

# the hypothesis mentions the number of goals scored by Real Madrid against Real Murcia, which is also mentioned in the premise
if goals_hypothesis!= goals_premise:
    # check if the number of goals from the hypothesis contradicts the number of goals in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
