# Premise: Alice can bake a pie in 5 minutes.
# Hypothesis: Alice can bake a pie in less than 7 minutes.
# Golden Label: entailment

baking_time_premise = 5
baking_time_hypothesis = 7

# The hypothesis refers to the time Alice takes to bake a pie, also mentioned in the premise
if baking_time_hypothesis <= baking_time_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif baking_time_hypothesis > baking_time_premise:
    # if the premise value is less than the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if none of the above conditions are met, the relationship is neutral
    label = "neutral"

print(label)

