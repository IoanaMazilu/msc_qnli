portion_premise = 7/12
portion_hypothesis = 4/12

# the hypothesis refers to the portion of money Anup was asked to find in the premise
if portion_hypothesis >= portion_premise:
    # check if the hypothesis value contradicts the exact portion 'portion_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
