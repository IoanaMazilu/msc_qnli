times_as_old_premise = 5/3
times_as_old_hypothesis = 1/3

# the hypothesis refers to the ratio of their ages in the future, mentioned in the premise
if times_as_old_hypothesis != times_as_old_premise:
    # check if the hypothesis value contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
