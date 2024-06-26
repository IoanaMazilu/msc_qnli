# Define variables for the numerical entities in the premise and hypothesis
petrol_scooter_premise = 0.8
house_rent_premise = 0.12
food_premise = 0.8
petrol_scooter_hypothesis = 0.3
house_rent_hypothesis = 0.12
food_hypothesis = 0.8

# Extract all quantities as valid numbers
petrol_scooter_premise = float(petrol_scooter_premise)
house_rent_premise = float(house_rent_premise)
food_premise = float(food_premise)
petrol_scooter_hypothesis = float(petrol_scooter_hypothesis)
house_rent_hypothesis = float(house_rent_hypothesis)
food_hypothesis = float(food_hypothesis)

# Check if the hypothesis values contradict the premise
if petrol_scooter_hypothesis <= petrol_scooter_premise:
    # The hypothesis value contradicts the estimate of less than 'petrol_scooter_premise'
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # The number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
elif food_hypothesis!= food_premise:
    # The number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
