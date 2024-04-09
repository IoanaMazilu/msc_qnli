george_car_premise = 7
george_car_hypothesis = 8

# the hypothesis refers to the amount of oil required for each cylinder used in George's car
if george_car_hypothesis > george_car_premise:
    # the hypothesis explicitly entails the premise
    label = "entailment"
elif george_car_hypothesis == george_car_premise:
    # the hypothesis and premise are consistent with each other
    label = "neutral"
else:
    # the hypothesis contradicts the premise
    label = "contradiction"

print(label)
