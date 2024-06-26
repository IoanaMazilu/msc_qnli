recommendations_premise = 100
recommendations_hypothesis = 100

# the hypothesis mentions the number of recommendations, which is also referenced in the premise
if recommendations_hypothesis > recommendations_premise:
    # check if the number of recommendations in the hypothesis contradicts the premise
    label = "contradiction"
elif recommendations_hypothesis < recommendations_premise:
    # check if the number of recommendations in the hypothesis is lower than in the premise
    label = "contradiction"
else:
    # if the number of recommendations in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
