# Premise: Compute how many more pies Alice can bake than Bob in more than 10 minutes.
# Hypothesis: Compute how many more pies Alice can bake than Bob in 60 minutes.
# Golden Label: neutral

baking_time_premise = 10
baking_time_hypothesis = 60

# the hypothesis refers to the time in which Alice and Bob can bake pies, mentioned also in the premise
if baking_time_hypothesis <= baking_time_premise:
    # check if the 'baking_time_hypothesis' contradicts the estimate of more than 'baking_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Alice and Bob can bake pies
    # any time greater than 'baking_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

