car_oil_premise = 7
car_oil_hypothesis = 8

# the hypothesis talks about the amount of oil needed for each cylinder in George's car, referenced also in the premise
if car_oil_hypothesis <= car_oil_premise:
    # check if the hypothesis value contradicts the estimate of more than 'car_oil_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of oil needed, any amount greater than 'car_oil_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
