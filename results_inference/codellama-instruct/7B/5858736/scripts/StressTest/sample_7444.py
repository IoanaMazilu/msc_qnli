# Define variables for the numerical entities in the premise and hypothesis
petrol_spent_premise = 60
house_rent_premise = 14
food_spent_premise = 100 - (60 + 14)

petrol_spent_hypothesis = 30
house_rent_hypothesis = 14
food_spent_hypothesis = 100 - (30 + 14)

# Check if the hypothesis values contradict the premise
if petrol_spent_hypothesis > petrol_spent_premise:
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    label = "contradiction"
elif food_spent_hypothesis!= food_spent_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
