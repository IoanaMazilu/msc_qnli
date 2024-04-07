# Premise: Compute how many more pies Alice can bake than Bob in 60 minutes.
# Hypothesis: Compute how many more pies Alice can bake than Bob in more than 10 minutes.
# Golden Label: entailment

baking_time_premise = 60
baking_time_hypothesis = 10

# the hypothesis asks for the difference in the number of pies Alice and Bob can bake in a certain time
# both premise and hypothesis refer to the same concept, but different time frames
if baking_time_hypothesis >= baking_time_premise:
    # check if the hypothesis time contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # the premise gives an explicit time for baking, but the hypothesis only gives a minimum time
    # any time greater than 'baking_time_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

