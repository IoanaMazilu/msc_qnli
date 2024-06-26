speed_premise = 30
speed_hypothesis = 30

# the hypothesis refers to the speed of Cara while driving from City A to City B mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis is less than the speed in the premise, it is not contradictory
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
