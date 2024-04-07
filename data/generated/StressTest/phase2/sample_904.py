# Premise: Mike can catch less than 60 fish in one hour, Jim can catch twice as much and Bob can catch 50% more than Jim.
# Hypothesis: Mike can catch 30 fish in one hour, Jim can catch twice as much and Bob can catch 50% more than Jim.
# Golden Label: neutral

mike_fish_premise = 60
mike_fish_hypothesis = 30
jim_fish_premise = 2 * mike_fish_premise
bob_fish_premise = 1.5 * jim_fish_premise
jim_fish_hypothesis = 2 * mike_fish_hypothesis
bob_fish_hypothesis = 1.5 * jim_fish_hypothesis

# the hypothesis refers to the number of fish that Mike, Jim and Bob can catch in one hour, as mentioned in the premise
if mike_fish_hypothesis >= mike_fish_premise:
    # check if 'mike_fish_hypothesis' contradicts the premise that Mike can catch less than 'mike_fish_premise' fish 
    label = "contradiction"
elif jim_fish_hypothesis != jim_fish_premise or bob_fish_hypothesis != bob_fish_premise:
    # check if the number of fish Jim and Bob can catch in the hypothesis contradicts the number of fish they can catch according to the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

