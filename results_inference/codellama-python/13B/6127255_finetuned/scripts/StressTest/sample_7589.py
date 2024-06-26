# Scores in different subjects as per premise
french_premise = 86
geography_premise = 75
art_premise = 72
history_premise = 63
PE_premise = 65

# Scores in different subjects as per hypothesis
french_hypothesis = 86
geography_hypothesis = 75
art_hypothesis = 72
history_hypothesis = 63
PE_hypothesis = 65

# Average score as per premise
average_score_premise = (french_premise + geography_premise + art_premise + history_premise + PE_premise) / 5

# Average score as per hypothesis
average_score_hypothesis = (french_hypothesis + geography_hypothesis + art_hypothesis + history_hypothesis + PE_hypothesis) / 5

# Check if the average score as per hypothesis contradicts the average score as per premise
if average_score_hypothesis!= average_score_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
