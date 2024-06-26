investments_premise = 305000
investments_hypothesis = 305000
life_insurance_premise = 104000
life_insurance_hypothesis = 104000
car_premise = 4900
car_hypothesis = 1900
house_premise = 75000
house_hypothesis = 75000

# the hypothesis refers to the assets and their values in the premise
if investments_premise != investments_hypothesis or life_insurance_premise != life_insurance_hypothesis or house_premise != house_hypothesis:
    # check if the values in the hypothesis contradict the values in the premise
    label = "contradiction"
elif car_hypothesis > car_premise:
    # check if the selling price of the car in the hypothesis contradicts the selling price in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
