# Define variables for premise and hypothesis
petrol_income_premise = 80
petrol_income_hypothesis = 30
house_rent_premise = 12
house_rent_hypothesis = 12
food_premise = 80
food_hypothesis = 80

# Check for entailment, contradiction, or neutrality
if petrol_income_hypothesis <= petrol_income_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'petrol_income_premise'
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # Check if the number of house rent in the hypothesis contradicts the number of house rent reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
