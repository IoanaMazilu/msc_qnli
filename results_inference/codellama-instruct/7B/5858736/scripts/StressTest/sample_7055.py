# Define variables for the numerical entities in the premise and hypothesis
amar_score_premise = 64
bhavan_score_premise = 36
chetan_score_premise = 44

amar_score_hypothesis = 24
bhavan_score_hypothesis = 36
chetan_score_hypothesis = 44

# Check if the hypothesis values contradict the premise values
if amar_score_hypothesis!= amar_score_premise:
    label = "contradiction"
elif bhavan_score_hypothesis!= bhavan_score_premise:
    label = "contradiction"
elif chetan_score_hypothesis!= chetan_score_premise:
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
