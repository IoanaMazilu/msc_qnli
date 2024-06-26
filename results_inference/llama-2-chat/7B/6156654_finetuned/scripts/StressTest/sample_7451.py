petrol_income_bhanu = 30
petrol_income_hypothesis = 30

house_rent_bhanu = 12
house_rent_hypothesis = 12

food_income_bhanu = 100 - (petrol_income_bhanu + house_rent_bhanu)
food_income_hypothesis = 100 - (petrol_income_hypothesis + house_rent_hypothesis)

# the hypothesis talks about Bhanu's spending on petrol, house rent, and food
if petrol_income_bhanu!= petrol_income_hypothesis:
    # check if the percentage of income spent on petrol in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif house_rent_bhanu!= house_rent_hypothesis:
    # check if the percentage of income spent on house rent in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif food_income_bhanu!= food_income_hypothesis:
    # check if the percentage of income spent on food in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage of income spent on petrol, house rent, and food in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
