bake_time_premise = 6
bake_time_hypothesis = 1

# the hypothesis refers to the time Bob takes to bake a pie, which is also mentioned in the premise
if bake_time_hypothesis >= bake_time_premise:
    # check if the hypothesis value contradicts the baking time stated in the premise
    label = "contradiction"
else:
    # if the baking time in the hypothesis is less than the one in the premise, we can infer entailment
    label = "entailment"

print(label)
