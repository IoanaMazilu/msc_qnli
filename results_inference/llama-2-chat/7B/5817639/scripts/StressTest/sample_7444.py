# Premise: Bhanu spends less than 60% of his income on petrol on scooter 14% of the remaining on house rent and the balance on food.
petrol_income_premise = 60
petrol_income_hypothesis = 30
house_rent_premise = 14
house_rent_hypothesis = 14
food_premise = float(petrol_income_premise * 0.6)
food_hypothesis = float(petrol_income_hypothesis * 0.3)

# the hypothesis talks about the distribution of Bhanu's income, which is also mentioned in the premise
if petrol_income_hypothesis <= petrol_income_premise:
    # check if the hypothesis value contradicts the estimate of less than 'petrol_income_premise'
    label = "contradiction"
elif house_rent_hypothesis!= house_rent_premise:
    # check if the number of house rent in the hypothesis contradicts the number of house rent reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
