goals_premise = 4
goals_hypothesis = 4

# the hypothesis mentions the number of goals scored by Arsenal, which is also mentioned in the premise
if goals_hypothesis!= goals_premise:
    # check if the number of goals in the hypothesis contradicts the number of goals reported in the premise
    label = "contradiction"
else:
    # if the number of goals in the hypothesis does not contradict the number of goals in the premise, we can infer entailment
    label = "entailment"

print(label)
