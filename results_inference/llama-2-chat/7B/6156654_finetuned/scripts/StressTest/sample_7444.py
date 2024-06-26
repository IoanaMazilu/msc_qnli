petrol_income_percentage_premise = 60
petrol_income_percentage_hypothesis = 30
house_rent_percentage_premise = 14
house_rent_percentage_hypothesis = 14
food_percentage_premise = 14
food_percentage_hypothesis = 14

# the hypothesis talks about Bhanu's spending on petrol, house rent, and food, which are also mentioned in the premise
if petrol_income_percentage_hypothesis <= petrol_income_percentage_premise:
    # check if the hypothesis value contradicts the premise value for petrol income percentage
    label = "contradiction"
elif house_rent_percentage_hypothesis!= house_rent_percentage_premise:
    # check if the hypothesis value contradicts the premise value for house rent percentage
    label = "contradiction"
elif food_percentage_hypothesis!= food_percentage_premise:
    # check if the hypothesis value contradicts the premise value for food percentage
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
