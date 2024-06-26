petrol_income_premise = 30
petrol_income_hypothesis = 30
house_rent_premise = 14
house_rent_hypothesis = 14
food_balance_premise = 60
food_balance_hypothesis = 60

# the hypothesis talks about the percentage of income spent on petrol, house rent and food, referenced also in the premise
if petrol_income_hypothesis <= petrol_income_premise:
    # check if the hypothesis value contradicts the estimate of more than 'petrol_income_premise'
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # check if the number of house rent in the hypothesis contradicts the number of house rent reported in the premise
    label = "contradiction"
elif food_balance_hypothesis!= food_balance_premise:
    # check if the number of food in the hypothesis contradicts the number of food reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
