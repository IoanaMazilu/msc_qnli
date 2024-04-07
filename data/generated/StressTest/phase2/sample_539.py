# Premise: Shridhar is 3:2.
# Hypothesis: Shridhar is 7:2.
# Golden Label: contradiction

shridhar_premise = 3/2
shridhar_hypothesis = 7/2

# The hypothesis refers to the ratio of Shridhar mentioned in the premise
if shridhar_hypothesis != shridhar_premise:
    # check if the ratio of Shridhar in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

