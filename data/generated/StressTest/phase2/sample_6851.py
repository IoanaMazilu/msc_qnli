# Premise: Billy has 10 apples.
# Hypothesis: Billy has less than 10 apples.
# Golden Label: contradiction

apples_billy_premise = 10
apples_billy_hypothesis = 10

# the hypothesis refers to the number of apples Billy has, as mentioned in the premise
if apples_billy_hypothesis < apples_billy_premise:
    # check if the estimate of 'apples_billy_hypothesis' contradicts the number of apples in the premise
    label = "contradiction"
elif apples_billy_hypothesis > apples_billy_premise:
    # check if the number of apples in the hypothesis contradicts the number of apples reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

