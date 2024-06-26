sameer_age_premise = 2
anand_age_premise = 3
sameer_age_hypothesis = 5
anand_age_hypothesis = 4

# the hypothesis talks about the ratio of ages of Sameer and Anand, which is also mentioned in the premise
if sameer_age_hypothesis / sameer_age_premise!= anand_age_hypothesis / anand_age_premise:
    # check if the ratio of ages in the hypothesis contradicts the ratio of ages in the premise
    label = "contradiction"
elif sameer_age_hypothesis / sameer_age_premise == anand_age_hypothesis / anand_age_premise:
    # if the ratio of ages in the hypothesis matches the ratio of ages in the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and ratios do not contradict the premise values and ratios, we can infer neutrality
    label = "neutral"

print(label)
