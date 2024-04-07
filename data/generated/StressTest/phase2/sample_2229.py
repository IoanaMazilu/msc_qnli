# Premise: One year ago, the ratio of Roonie’s and Ronaldo’s age was 6:7 respectively.
# Hypothesis: One year ago, the ratio of Roonie’s and Ronaldo’s age was less than 7:7 respectively.
# Golden Label: entailment

roonie_ronaldo_ratio_premise = 6/7
roonie_ronaldo_ratio_hypothesis = 7/7

# the hypothesis refers to the ratio of ages of Roonie and Ronaldo one year ago mentioned in the premise
if roonie_ronaldo_ratio_premise >= roonie_ronaldo_ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)

