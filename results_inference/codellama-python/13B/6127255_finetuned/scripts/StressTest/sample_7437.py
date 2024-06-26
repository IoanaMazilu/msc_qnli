horses_premise = 3
horses_hypothesis = 4
total_horses = 25

# the hypothesis refers to the number of fastest horses needed for the Kentucky Derby, mentioned in the premise
if horses_hypothesis <= horses_premise:
    # check if the hypothesis value contradicts the number of fastest horses in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
