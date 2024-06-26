# Define the variables for the number of shoes Marcella has
marcella_shoes_premise = 27
marcella_shoes_hypothesis = 17

# Check if the number of shoes in the hypothesis contradicts the number of shoes in the premise
if marcella_shoes_hypothesis >= marcella_shoes_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)