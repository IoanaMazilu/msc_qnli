# Define variables with representative names for the numerical entities in both inputs
amar_score_premise = 84
bhavan_score_premise = 36
chetan_score_premise = 44

amar_score_hypothesis = 64
bhavan_score_hypothesis = 36
chetan_score_hypothesis = 44

# Extract all quantities as valid numbers

# Check if the hypothesis values contradict the premise ones
if amar_score_hypothesis > amar_score_premise:
    label = "contradiction"
elif bhavan_score_hypothesis!= bhavan_score_premise:
    label = "contradiction"
elif chetan_score_hypothesis!= chetan_score_premise:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
