militants_killed_premise = 11
soldiers_killed_premise = 6
total_killed_hypothesis = 17

# Add the number of militants and soldiers killed in the premise
total_killed_premise = militants_killed_premise + soldiers_killed_premise

# Compare the total number of people killed in the hypothesis with the total number in the premise
if total_killed_hypothesis == total_killed_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
