water_storage_premise = 7
water_storage_hypothesis = 3

# the hypothesis refers to the amount of water Jill has stored, also mentioned in the premise
if water_storage_hypothesis > water_storage_premise:
    # check if the amount of water in the hypothesis contradicts the amount of water reported in the premise
    label = "contradiction"
elif water_storage_hypothesis < water_storage_premise:
    # check if the amount of water in the hypothesis is less than the amount of water reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
