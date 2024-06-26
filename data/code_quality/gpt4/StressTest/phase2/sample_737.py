T_premise = 75
T_hypothesis = 75
multiplier_premise = 5/9
multiplier_hypothesis = 5/9

# the hypothesis refers to the formula of converting temperature from Kelvin to Fahrenheit mentioned in the premise
if T_hypothesis != T_premise:
    # check if the value of T in the hypothesis contradicts the value of T reported in the premise
    label = "contradiction"
elif multiplier_hypothesis < multiplier_premise:
    # check if the multiplier in the hypothesis contradicts the multiplier reported in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, but the hypothesis introduces an estimate 'more than multiplier_premise' that is not explicitly entailed by the premise
    label = "neutral"

print(label)
