people_premise = 15
people_hypothesis = 15

# the hypothesis refers to the same number of people as in the premise
if people_hypothesis < people_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
elif people_hypothesis == people_premise:
    # check if the number of people in the hypothesis equals the number of people in the premise
    label = "neutral"
else:
    # if the number of people in the hypothesis is greater than the number of people in the premise, we can infer entailment
    label = "entailment"

print(label)
