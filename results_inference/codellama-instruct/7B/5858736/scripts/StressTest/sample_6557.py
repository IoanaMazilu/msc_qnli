# Define variables for the premise
england_france_premise = 0
england_italy_premise = 6
france_italy_premise = 11

# Define variables for the hypothesis
england_france_hypothesis = 0
england_italy_hypothesis = 2
france_italy_hypothesis = 11

# Check if the hypothesis values contradict the premise
if england_france_hypothesis!= england_france_premise:
    label = "contradiction"
elif england_italy_hypothesis!= england_italy_premise:
    label = "contradiction"
elif france_italy_hypothesis!= france_italy_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
