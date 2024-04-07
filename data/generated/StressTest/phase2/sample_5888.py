# Premise: When Anusha reached the goal post, Banu was 10 m behind.
# Hypothesis: When Anusha reached the goal post, Banu was more than 10 m behind.
# Golden Label: contradiction

banu_behind_premise = 10
banu_behind_hypothesis = 10

# the hypothesis refers to the distance Banu is behind when Anusha reached the goal post, which is mentioned in the premise
if banu_behind_hypothesis > banu_behind_premise:
    # check if the hypothesis, which is more than 'banu_behind_premise', contradicts the distance mentioned in the premise
    label = "contradiction"
elif banu_behind_hypothesis < banu_behind_premise:
    # check if the hypothesis, which is less than 'banu_behind_premise', contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

