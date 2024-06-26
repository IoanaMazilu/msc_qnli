car_oil_premise = 8
car_oil_hypothesis = 10

# the hypothesis talks about the amount of oil needed for George's car, which is also referenced in the premise
if car_oil_hypothesis <= car_oil_premise:
    # check if the hypothesis value contradicts the estimate of 8 ounces of oil for each cylinder in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of oil needed, and any amount greater than 8 ounces is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
