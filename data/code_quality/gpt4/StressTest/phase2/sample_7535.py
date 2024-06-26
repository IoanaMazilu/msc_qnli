leo_gain_premise = 10
leo_gain_hypothesis = 80
percentage_increase = 50

# the hypothesis refers to the same situation as the premise, but with a different amount of weight gain for Leo
if leo_gain_hypothesis != leo_gain_premise:
    # check if the amount of weight Leo gains in the hypothesis contradicts the amount of weight gain mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates are the same as the premise ones, we can infer entailment
    label = "entailment"

print(label)
