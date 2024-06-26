car_ac_ratio_premise = 2/2
car_ac_ratio_hypothesis = 3/2

# the hypothesis talks about the ratio of the prices of a car and AC, referenced also in the premise
if car_ac_ratio_hypothesis <= car_ac_ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'car_ac_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of the prices of a car and AC
    # any ratio greater than 'car_ac_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
