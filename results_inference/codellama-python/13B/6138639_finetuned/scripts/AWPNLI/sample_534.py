birds_on_fence_premise = 12.0
birds_fly_away_premise = 8.0
birds_on_fence_hypothesis = 4.0

# the hypothesis refers to the number of birds on the fence, which is also mentioned in the premise
# compute the number of birds left on the fence in the premise
birds_left_on_fence_premise = birds_on_fence_premise - birds_fly_away_premise
if birds_on_fence_hypothesis!= birds_left_on_fence_premise:
    # check if the number of birds on the fence in the hypothesis contradicts the number of birds left on the fence from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
