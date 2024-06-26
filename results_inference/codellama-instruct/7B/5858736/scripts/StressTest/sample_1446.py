# Define variables for the numerical entities in both inputs
people_dead_premise = 5
people_left_premise = 15
people_dead_hypothesis = 4
people_left_hypothesis = 15

# Extract all quantities as valid numbers
people_dead_premise = float(people_dead_premise) / 100
people_left_premise = float(people_left_premise) / 100
people_dead_hypothesis = float(people_dead_hypothesis) / 100
people_left_hypothesis = float(people_left_hypothesis) / 100

# Check if the hypothesis values contradict the premise values
if people_dead_hypothesis <= people_dead_premise:
    # The hypothesis value contradicts the premise value, so the hypothesis is a contradiction
    label = "contradiction"
elif people_left_hypothesis!= people_left_premise:
    # The number of people who left the village in the hypothesis contradicts the number of people who left the village in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
