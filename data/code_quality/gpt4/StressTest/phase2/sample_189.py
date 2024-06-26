# Defining the ratio of ages in the premise and hypothesis
ratio_premise = 5 / 9
ratio_hypothesis = 6 / 9

# the hypothesis refers to the ratio of ages mentioned in the premise
if ratio_premise >= ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
