# Define variables with representative names for the numerical entities in both inputs
friends_john_premise = 6
friends_john_hypothesis = 5
passengers_car_premise = 5
passengers_car_hypothesis = 4

# Extract all quantities as valid numbers (integers or floats)
friends_john_premise = int(friends_john_premise)
friends_john_hypothesis = int(friends_john_hypothesis)
passengers_car_premise = int(passengers_car_premise)
passengers_car_hypothesis = int(passengers_car_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if friends_john_hypothesis <= friends_john_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'friends_john_premise'
    label = "contradiction"
elif passengers_car_hypothesis <= passengers_car_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'passengers_car_premise'
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
