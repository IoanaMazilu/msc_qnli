sameer_age_premise = 5
anand_age_premise = 4
sameer_age_hypothesis = 3
anand_age_hypothesis = 4

# the hypothesis refers to the ratio of their ages
if sameer_age_hypothesis / anand_age_hypothesis > 3 / 4:
    # the hypothesis implies a different ratio than the premise
    label = "contradiction"
elif sameer_age_hypothesis == anand_age_hypothesis:
    # the hypothesis and premise have the same ratio, no entailment or contradiction
    label = "neutral"
else:
    # the hypothesis implies a ratio greater than the premise, so entailment
    label = "entailment"

print(label)
