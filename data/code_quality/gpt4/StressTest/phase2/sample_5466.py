investment_premise = 305000
investment_hypothesis = 305000
insurance_premise = 104000
insurance_hypothesis = 104000
car_premise = 1900
car_hypothesis = 4900
house_premise = 75000
house_hypothesis = 75000

# the hypothesis refers to the value of the assets mentioned in the premise
if investment_premise != investment_hypothesis:
    # check if the value of the investments in the hypothesis contradicts the value in the premise
    label = "contradiction"
elif insurance_premise != insurance_hypothesis:
    # check if the value of the life insurance in the hypothesis contradicts the value in the premise
    label = "contradiction"
elif car_premise >= car_hypothesis:
    # check if the value of the old car in the hypothesis contradicts the value in the premise
    label = "contradiction"
elif house_premise != house_hypothesis:
    # check if the value of the older house in the hypothesis contradicts the value in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
