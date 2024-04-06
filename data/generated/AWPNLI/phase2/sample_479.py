# Premise: Mike picked 7.0 apples, Nancy picked 3.0 apples, but Keith ate 6.0 apples and 4.0 pears, at the farm.
# Hypothesis: 1.0 apple is left.
# Golden Label: contradiction

mike_apples_premise = 7.0
nancy_apples_premise = 3.0
keith_apples_premise = 6.0
apples_left_hypothesis = 1.0

# the hypothesis refers to the number of apples left, which can be calculated from the premise
# compute the total number of apples left in the premise
apples_left_premise = mike_apples_premise + nancy_apples_premise - keith_apples_premise
if apples_left_hypothesis != apples_left_premise:
    # check if the number of apples left in the hypothesis contradicts the number of apples left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

