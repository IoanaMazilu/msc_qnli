# Define variables for the numerical entities in the premise and hypothesis
petrol_spent_premise = 30
house_rent_spent_premise = 14
food_spent_premise = 100 - (petrol_spent_premise + house_rent_spent_premise)

petrol_spent_hypothesis = 35
house_rent_spent_hypothesis = 14
food_spent_hypothesis = 100 - (petrol_spent_hypothesis + house_rent_spent_hypothesis)

# Check if the hypothesis values contradict the premise
if petrol_spent_hypothesis > petrol_spent_premise:
    label = "contradiction"
elif house_rent_spent_hypothesis!= house_rent_spent_premise:
    label = "contradiction"
elif food_spent_hypothesis!= food_spent_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
