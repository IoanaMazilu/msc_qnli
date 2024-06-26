 ratio_premise = 2/2
ratio_hypothesis = 3/2

# the hypothesis talks about the ratio of car and AC prices, referenced also in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
