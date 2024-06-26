petrol_income_premise = 30
petrol_income_hypothesis = 60
house_rent_premise = 14
house_rent_hypothesis = 14
food_income_premise = 100 - petrol_income_premise - house_rent_premise
food_income_hypothesis = 100 - petrol_income_hypothesis - house_rent_hypothesis

# the hypothesis talks about the percentage of income spent on petrol, house rent and food
# the premise gives the exact percentages spent on petrol, house rent and food
if petrol_income_hypothesis >= petrol_income_premise:
    # check if the hypothesis value contradicts the percentage of income spent on petrol in the premise
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # check if the number of house rent in the hypothesis contradicts the number of house rent reported in the premise
    label = "contradiction"
elif food_income_hypothesis!= food_income_premise:
    # check if the number of food income in the hypothesis contradicts the number of food income reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
