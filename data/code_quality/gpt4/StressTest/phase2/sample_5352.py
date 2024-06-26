water_drink_premise = 8
water_drink_hypothesis = 2
times_drink_premise = 8
times_drink_hypothesis = 8

# the hypothesis refers to the amount of water Jimmy drinks and the number of times this drinking occurs mentioned in the premise
if water_drink_hypothesis >= water_drink_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif times_drink_hypothesis != times_drink_premise:
    # check if the number of times Jimmy drinks in the hypothesis contradicts the number of drinking times reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
