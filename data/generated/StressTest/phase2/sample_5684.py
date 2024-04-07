# Premise: 6000 among John, Jose & Binoy in the ration 2:4:6.
# Hypothesis: 8000 among John, Jose & Binoy in the ration 2:4:6.
# Golden Label: contradiction

total_money_premise = 6000
total_money_hypothesis = 8000

# the hypothesis refers to the same money distribution among the same people as the premise
if total_money_premise != total_money_hypothesis:
    # check if the total money in the hypothesis contradicts the total money reported in the premise
    label = "contradiction"
else:
    # if the total money in the hypothesis does not contradict the total money in the premise, we can infer entailment
    label = "entailment"

print(label)

