# Define variables with representative names for the numerical entities in both inputs
petrol_premise = 0.3 * income_premise  # calculate the percentage of income spent on petrol in the premise
petrol_hypothesis = 0.6 * income_hypothesis  # calculate the percentage of income spent on petrol in the hypothesis
house_rent_premise = 0.14 * (1 - petrol_premise)  # calculate the percentage of income spent on house rent in the premise
house_rent_hypothesis = 0.14 * (1 - petrol_hypothesis)  # calculate the percentage of income spent on house rent in the hypothesis
food_premise = income_premise - petrol_premise - house_rent_premise  # calculate the percentage of income spent on food in the premise
food_hypothesis = income_hypothesis - petrol_hypothesis - house_rent_hypothesis  # calculate the percentage of income spent on food in the hypothesis

# Extract all quantities as valid numbers (integers or floats)
petrol_premise = float(petrol_premise)
petrol_hypothesis = float(petrol_hypothesis)
house_rent_premise = float(house_rent_premise)
house_rent_hypothesis = float(house_rent_hypothesis)
food_premise = float(food_premise)
food_hypothesis = float(food_hypothesis)

# Compare the variables and determine the label
if petrol_hypothesis <= petrol_premise:
    # Check if the estimate of 'petrol_hypothesis' contradicts the number of petrol spent in the premise
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # Check if the number of house rent in the hypothesis contradicts the number of house rent reported in the premise
    label = "contradiction"
elif food_hypothesis!= food_premise:
    # Check if the number of food spent in the hypothesis contradicts the number of food spent reported in the premise
    label = "neutral"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
