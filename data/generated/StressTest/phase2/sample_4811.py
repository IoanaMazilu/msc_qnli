# Premise: Compute how many more pies Alice can bake than Bob in 60 minutes.
# Hypothesis: Compute how many more pies Alice can bake than Bob in 80 minutes.
# Golden Label: contradiction

baking_time_premise = 60
baking_time_hypothesis = 80

# the hypothesis asks for the comparison of pies baked by Alice and Bob, but in a different time than the premise
if baking_time_hypothesis != baking_time_premise:
    # the number of pies that can be baked in 'baking_time_hypothesis' might not be the same as in 'baking_time_premise'
    label = "neutral"
else:
    # if the baking time is the same in the hypothesis and premise, we could infer entailment, but this is not the case here
    pass

print(label)

