# Premise: Mike can catch 15 fish in one hour, Jim can catch twice as much and Bob can catch 50% more than Jim.
# Hypothesis: Mike can catch less than 25 fish in one hour, Jim can catch twice as much and Bob can catch 50% more than Jim.
# Golden Label: entailment

mike_catch_premise = 15
jim_catch_premise = mike_catch_premise * 2
bob_catch_premise = jim_catch_premise * 1.5

mike_catch_hypothesis = 25
jim_catch_hypothesis = mike_catch_hypothesis * 2
bob_catch_hypothesis = jim_catch_hypothesis * 1.5

# the hypothesis refers to the number of fish each person can catch in one hour
if mike_catch_premise >= mike_catch_hypothesis:
    # check if the estimate of 'mike_catch_hypothesis' contradicts the number of fish Mike can catch in the premise
    label = "contradiction"
elif jim_catch_premise != jim_catch_hypothesis:
    # check if the number of fish Jim can catch in the hypothesis contradicts the number of fish he can catch according to the premise
    label = "contradiction"
elif bob_catch_premise != bob_catch_hypothesis:
    # check if the number of fish Bob can catch in the hypothesis contradicts the number of fish he can catch according to the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

