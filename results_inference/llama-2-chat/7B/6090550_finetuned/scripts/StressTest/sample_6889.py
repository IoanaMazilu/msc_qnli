people_premise = 8
people_hypothesis = 6

# the hypothesis refers to the number of people that can be seated on a bench, which is also mentioned in the premise
if people_hypothesis >= people_premise:
    # check if the number of people in the hypothesis contradicts the premise
    label = "contradiction"
elif people_hypothesis < people_premise:
    # if the number of people in the hypothesis is less than the number of people in the premise, it is consistent with the premise
    label = "entailment"
else:
    # if the number of people in the hypothesis is equal to the number of people in the premise, it is neutral
    label = "neutral"

print(label)
