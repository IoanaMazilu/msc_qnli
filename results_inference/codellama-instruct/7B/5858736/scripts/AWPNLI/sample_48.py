# Define variables for the premise
men_bathing_suits_premise = 14797.0
women_bathing_suits_premise = 4969.0
total_bathing_suits_premise = men_bathing_suits_premise + women_bathing_suits_premise

# Define variables for the hypothesis
overall_bathing_suits_hypothesis = 19766.0

# Check if the hypothesis contradicts the premise
if overall_bathing_suits_hypothesis!= total_bathing_suits_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
