# Define variables for the numerical entities in both inputs
anita_days_premise = 18
indu_days_premise = 27
geeta_days_premise = 36
anita_days_hypothesis = 58
indu_days_hypothesis = 27
geeta_days_hypothesis = 36

# Extract all quantities as valid numbers
anita_days_premise = int(anita_days_premise)
indu_days_premise = int(indu_days_premise)
geeta_days_premise = int(geeta_days_premise)
anita_days_hypothesis = int(anita_days_hypothesis)
indu_days_hypothesis = int(indu_days_hypothesis)
geeta_days_hypothesis = int(geeta_days_hypothesis)

# Check if the hypothesis values contradict the premise
if anita_days_hypothesis <= anita_days_premise:
    label = "contradiction"
elif indu_days_hypothesis!= indu_days_premise:
    label = "contradiction"
elif geeta_days_hypothesis!= geeta_days_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
