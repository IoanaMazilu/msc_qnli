# Define variables for numerical entities in the premise and hypothesis
petrol_premise = 0.3 * income_premise  # 30% of income on petrol
house_rent_premise = 0.12 * (income_premise - petrol_premise)  # 12% of remaining on house rent
food_premise = income_premise - petrol_premise - house_rent_premise  # balance on food

# Define variables for numerical entities in the hypothesis
petrol_hypothesis = 0.4 * income_hypothesis  # more than 30% of income on petrol
house_rent_hypothesis = 0.12 * (income_hypothesis - petrol_hypothesis)  # 12% of remaining on house rent
food_hypothesis = income_hypothesis - petrol_hypothesis - house_rent_hypothesis

# Perform calculations
petrol_diff = petrol_hypothesis - petrol_premise
house_rent_diff = house_rent_hypothesis - house_rent_premise
food_diff = food_hypothesis - food_premise

# Check for contradictions
if petrol_diff > 0:
    label = "contradiction"  # hypothesis petrol estimate contradicts premise
elif house_rent_diff > 0:
    label = "contradiction"  # hypothesis house rent estimate contradicts premise
elif food_diff > 0:
    label = "contradiction"  # hypothesis food estimate contradicts premise
else:
    # No contradictions found, so entailment or neutrality
    if petrol_diff == 0 and house_rent_diff == 0 and food_diff == 0:
        label = "entailment"  # all estimates are consistent with the premise
    else:
        label = "neutral"  # estimates are consistent with the premise but cannot be explicitly entailed

print(label)
