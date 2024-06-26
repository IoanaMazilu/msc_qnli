speed_premise = 10
speed_hypothesis = 60

# the hypothesis refers to the speed of Lindy mentioned in the premise
if speed_hypothesis < speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif speed_hypothesis == speed_premise:
    # check if the speed in the hypothesis is the same as the speed in the premise
    label = "entailment"
else:
    # if the speed in the hypothesis is higher than the speed in the premise, it does not contradict the premise but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
