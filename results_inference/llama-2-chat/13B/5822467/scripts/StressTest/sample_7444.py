# Define variables for the numerical entities in the premise and hypothesis
petrol_premise = 14
house_rent_premise = 60 - petrol_premise
food_premise = house_rent_premise - 14

# Define variables for the numerical entities in the hypothesis
petrol_hypothesis = 30
house_rent_hypothesis = 60 - petrol_hypothesis
food_hypothesis = house_rent_hypothesis - 14

# Check if the hypothesis values contradict the premise values
if petrol_hypothesis > petrol_premise:
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    label = "contradiction"
elif food_hypothesis!= food_premise:
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
