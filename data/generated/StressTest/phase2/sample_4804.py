# Premise: Alice can bake a pie in less than 7 minutes.
# Hypothesis: Alice can bake a pie in 5 minutes.
# Golden Label: neutral

bake_time_premise = 7
bake_time_hypothesis = 5

# the hypothesis refers to the time it takes for Alice to bake a pie, mentioned also in the premise
if bake_time_hypothesis >= bake_time_premise:
    # check if the hypothesis time contradicts the premise of less than 'bake_time_premise' minutes
    label = "contradiction"
else:
    # the premise gives only an estimate for the baking time
    # any baking time less than 'bake_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

