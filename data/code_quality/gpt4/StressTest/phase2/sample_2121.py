classes_premise = 3
classes_hypothesis = 1

# the hypothesis refers to the number of Professor Wang's classes mentioned in the premise
if classes_hypothesis >= classes_premise:
    # check if the hypothesis value contradicts the number of classes in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
