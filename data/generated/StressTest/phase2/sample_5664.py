# Premise: If it takes Darcy a total of 5 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Hypothesis: If it takes Darcy a total of more than 2 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Golden Label: entailment

commute_difference_premise = 5
commute_difference_hypothesis = 2

# the hypothesis refers to the time difference between Darcy's commute methods mentioned in the premise
if commute_difference_hypothesis >= commute_difference_premise:
    # check if the hypothesis value contradicts the given 'commute_difference_premise'
    label = "contradiction"
elif commute_difference_hypothesis < commute_difference_premise:
    # check if the hypothesis value is less than the premise value
    # any value between 2 and 5 could be consistent with both the premise and hypothesis
    label = "neutral"
else:
    # if the hypothesis value is exactly the same as the premise value, we can infer entailment
    label = "entailment"

print(label)

