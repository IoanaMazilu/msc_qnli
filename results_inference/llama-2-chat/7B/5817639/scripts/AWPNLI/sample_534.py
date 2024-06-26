birds_on_fence_premise = float(12.0)
birds_fly_away_premise = float(8.0)
birds_on_fence_hypothesis = float(4.0)

# compare the number of birds on the fence in the hypothesis with the number in the premise
if birds_on_fence_hypothesis >= birds_on_fence_premise:
    # check if the number of birds on the fence in the hypothesis contradicts the estimate from the premise
    label = "contradiction"
elif birds_on_fence_hypothesis < birds_on_fence_premise:
    # if the number of birds on the fence in the hypothesis is less than the estimate from the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value and estimate do not contradict the premise value, we can infer neutrality
    label = "neutral"

print(label)
