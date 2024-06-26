borrowed_annually_premise = 5000
borrowed_annually_hypothesis = 3000

# the hypothesis refers to the amount of money Dana borrows annually for college, mentioned in the premise
if borrowed_annually_hypothesis != borrowed_annually_premise:
    # check if the amount in the hypothesis contradicts the amount mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
