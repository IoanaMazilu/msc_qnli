men_premise = 100
men_hypothesis = 600

# the hypothesis refers to the number of men employed by NHAI mentioned in the premise
if men_hypothesis <= men_premise:
    # check if the hypothesis value contradicts the number of men employed in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
