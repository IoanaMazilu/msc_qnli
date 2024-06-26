# Define variables for the numerical entities in the premise and hypothesis
petrol_premise = 0.3 * income_premise  # 30% of income on petrol
house_rent_premise = 0.14 * (1 - petrol_premise)  # 14% of remaining on house rent
food_premise = income_premise - petrol_premise - house_rent_premise  # balance on food

# Define variables for the numerical entities in the hypothesis
petrol_hypothesis = 0.4 * income_hypothesis  # more than 30% of income on petrol
house_rent_hypothesis = 0.14 * (1 - petrol_hypothesis)  # 14% of remaining on house rent
food_hypothesis = income_hypothesis - petrol_hypothesis - house_rent_hypothesis

# Check if the hypothesis values contradict the premise values
if petrol_hypothesis > petrol_premise:
    # The hypothesis value for petrol is greater than the premise value, so there is a contradiction
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # The hypothesis value for house rent is different from the premise value, so there is a contradiction
    label = "contradiction"
elif food_hypothesis!= food_premise:
    # The hypothesis value for food is different from the premise value, so there is a contradiction
    label = "contradiction"
else:
    # If all hypothesis values are consistent with the premise values, we can infer entailment
    label = "entailment"

print(label)
