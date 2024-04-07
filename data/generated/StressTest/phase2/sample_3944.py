# Premise: If it takes Darcy a total of 10 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Hypothesis: If it takes Darcy a total of less than 10 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Golden Label: contradiction

commute_difference_premise = 10
commute_difference_hypothesis = 10

# the hypothesis refers to the difference in commuting time mentioned in the premise
if commute_difference_hypothesis < commute_difference_premise:
    # check if the hypothesis value contradicts the value given in the premise
    label = "contradiction"
elif commute_difference_hypothesis > commute_difference_premise:
    # check if the hypothesis value exceeds the value given in the premise
    label = "contradiction"
else:
    # if the hypothesis value matches the premise value, we can infer entailment
    label = "entailment"

print(label)

