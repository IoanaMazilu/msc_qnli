# Define variables for the numerical entities in the premise and hypothesis
petrol_spent_premise = 0.3
house_rent_premise = 0.12
food_spent_premise = 1 - (petrol_spent_premise + house_rent_premise)

petrol_spent_hypothesis = 0.3
house_rent_hypothesis = 0.12
food_spent_hypothesis = 1 - (petrol_spent_hypothesis + house_rent_hypothesis)

# Check if the hypothesis values contradict the premise
if petrol_spent_hypothesis > petrol_spent_premise:
    label = "contradiction"
elif house_rent_hypothesis > house_rent_premise:
    label = "contradiction"
elif food_spent_hypothesis < food_spent_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
