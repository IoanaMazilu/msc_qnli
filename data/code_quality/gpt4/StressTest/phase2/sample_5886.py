banu_behind_premise = 10
banu_behind_hypothesis = 30

# the hypothesis refers to the distance of Banu from the goal post when Anusha reached it, mentioned also in the premise
if banu_behind_hypothesis < banu_behind_premise:
    # check if the hypothesis distance contradicts the actual distance of Banu from the goal post when Anusha reached it
    label = "contradiction"
else:
    # if the hypothesis distance does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
