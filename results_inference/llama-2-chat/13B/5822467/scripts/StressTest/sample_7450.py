# Define variables with representative names for the numerical entities in both inputs
petrol_premise = 0.12 * (100 - 80)
petrol_hypothesis = 0.3 * (100 - 80)
house_rent_premise = 12 * (100 - 80)
house_rent_hypothesis = 12 * (100 - 80)
food_premise = 100 - petrol_premise - house_rent_premise
food_hypothesis = 100 - petrol_hypothesis - house_rent_hypothesis

# Extract all quantities as valid numbers (integers or floats)
petrol_premise = int(petrol_premise * 100)
petrol_hypothesis = int(petrol_hypothesis * 100)
house_rent_premise = int(house_rent_premise * 100)
house_rent_hypothesis = int(house_rent_hypothesis * 100)
food_premise = int(food_premise * 100)
food_hypothesis = int(food_hypothesis * 100)

# Perform calculations and compare the variables
if petrol_hypothesis > petrol_premise:
    label = "entailment"
elif petrol_hypothesis <= petrol_premise:
    label = "neutral"
else:
    label = "contradiction"

if house_rent_hypothesis > house_rent_premise:
    label = "entailment"
elif house_rent_hypothesis <= house_rent_premise:
    label = "neutral"
else:
    label = "contradiction"

if food_hypothesis > food_premise:
    label = "entailment"
elif food_hypothesis <= food_premise:
    label = "neutral"
else:
    label = "contradiction"

print(label)
