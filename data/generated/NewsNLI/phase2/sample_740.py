# Premise: One assault occurred at the Church of Christ in Nations in Postikum, in Yobe province.
# Hypothesis: One attack was in Yobe province, the other in Borno state.
# Golden Label: neutral

attacks_premise = 1
attacks_hypothesis = 2

# the hypothesis mentions two attacks, one of which is also mentioned in the premise
if attacks_hypothesis != attacks_premise:
    # check if the number of attacks in the hypothesis contradicts the number of attacks reported in the premise
    label = "contradiction"
else:
    # if the number of attacks from the hypothesis matches the number of attacks in the premise, we can infer entailment
    label = "entailment"

print(label)
