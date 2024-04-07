# Premise: Mike can catch less than 25 fish in one hour, Jim can catch twice as much and Bob can catch 50% more than Jim.
# Hypothesis: Mike can catch 15 fish in one hour, Jim can catch twice as much and Bob can catch 50% more than Jim.
# Golden Label: neutral

mike_catch_premise = 25
jim_catch_premise = 2 * mike_catch_premise
bob_catch_premise = 1.5 * jim_catch_premise

mike_catch_hypothesis = 15
jim_catch_hypothesis = 2 * mike_catch_hypothesis
bob_catch_hypothesis = 1.5 * jim_catch_hypothesis

# the hypothesis refers to the number of fish each person can catch in one hour, mentioned in the premise
if mike_catch_hypothesis >= mike_catch_premise:
    # check if the number of fish Mike can catch in the hypothesis contradicts the premise
    label = "contradiction"
elif jim_catch_hypothesis != jim_catch_premise:
    # check if the number of fish Jim can catch in the hypothesis contradicts the premise
    label = "contradiction"
elif bob_catch_hypothesis != bob_catch_premise:
    # check if the number of fish Bob can catch in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

