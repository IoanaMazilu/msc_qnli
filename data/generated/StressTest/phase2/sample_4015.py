# Premise: If Leo gains less than 60 pounds, he will weigh 50% more than his sister Kendra.
# Hypothesis: If Leo gains 10 pounds, he will weigh 50% more than his sister Kendra.
# Golden Label: neutral

weight_gain_premise = 60
weight_gain_hypothesis = 10

# the hypothesis refers to the weight gain of Leo mentioned in the premise
if weight_gain_hypothesis >= weight_gain_premise:
    # check if the weight gain in the hypothesis contradicts the weight gain mentioned in the premise
    label = "contradiction"
else:
    # if the weight gain in the hypothesis is less than the weight gain in the premise, we can infer entailment
    label = "entailment"

print(label)

