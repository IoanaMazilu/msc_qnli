sameer_age_premise = float(1 / 4)
anand_age_premise = float(1 / 4)
sameer_age_hypothesis = 5 / 4
anand_age_hypothesis = 5 / 4

# the hypothesis refers to the ratio of their ages
if sameer_age_hypothesis > sameer_age_premise and anand_age_hypothesis > anand_age_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif sameer_age_hypothesis == sameer_age_premise and anand_age_hypothesis == anand_age_premise:
    # check if the hypothesis values do not contradict the premise ones
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
