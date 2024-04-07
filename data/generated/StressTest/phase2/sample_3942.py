# Premise: If it takes Darcy a total of 10 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Hypothesis: If it takes Darcy a total of less than 80 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Golden Label: entailment

commute_difference_premise = 10
commute_difference_hypothesis = 80

# the hypothesis refers to the difference in commute times mentioned in the premise
if commute_difference_hypothesis < commute_difference_premise:
    # check if the value of 'commute_difference_hypothesis' contradicts the difference in commute times stated in the premise
    label = "contradiction"
elif commute_difference_hypothesis > commute_difference_premise:
    # the hypothesis value is consistent with the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value equals the premise value, we can infer entailment
    label = "entailment"

print(label)
