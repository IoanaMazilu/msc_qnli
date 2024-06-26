leo_gain_premise = 10
leo_gain_hypothesis = 30
weight_percentage_difference = 50

# the hypothesis talks about the weight gain of Leo and its comparison to his sister's weight, referenced also in the premise
if leo_gain_hypothesis != leo_gain_premise:
    # check if the weight gain of Leo in the hypothesis contradicts the weight gain of Leo in the premise
    label = "contradiction"
else:
    # if the weight gain of Leo in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)
