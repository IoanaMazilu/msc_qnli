# Premise: Bob can bake a pie in more than 1 minutes.
# Hypothesis: Bob can bake a pie in 6 minutes.
# Golden Label: neutral

bake_time_premise = 1
bake_time_hypothesis = 6

# the hypothesis tells about the time Bob takes to bake a pie, which is also mentioned in the premise
if bake_time_hypothesis <= bake_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'bake_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the baking time
    # any baking time greater than 'bake_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

