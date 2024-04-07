# Premise: Mike can catch 15 fish in one hour, Jim can catch twice as much and Bob can catch 50% more than Jim.
# Hypothesis: Mike can catch less than 15 fish in one hour, Jim can catch twice as much and Bob can catch 50% more than Jim.
# Golden Label: contradiction

fish_mike_premise = 15
fish_jim_premise = 2 * fish_mike_premise
fish_bob_premise = 1.5 * fish_jim_premise

fish_mike_hypothesis = 15
fish_jim_hypothesis = 2 * fish_mike_hypothesis
fish_bob_hypothesis = 1.5 * fish_jim_hypothesis

# the hypothesis refers to the number of fish that Mike, Jim and Bob can catch in one hour
if fish_mike_premise >= fish_mike_hypothesis:
    # check if the estimate of 'fish_mike_hypothesis' contradicts the number of fish Mike can catch in the premise
    label = "contradiction"
elif fish_jim_premise != fish_jim_hypothesis or fish_bob_premise != fish_bob_hypothesis:
    # check if the number of fish Jim or Bob can catch in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

