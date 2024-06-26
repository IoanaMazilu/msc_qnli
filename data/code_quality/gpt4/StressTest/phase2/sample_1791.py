class_size_premise = 12
class_size_hypothesis = 42

# the hypothesis refers to the size of the class mentioned in the premise
if class_size_hypothesis < class_size_premise:
    # check if the estimate of 'class_size_hypothesis' contradicts the class size in the premise
    label = "contradiction"
elif class_size_hypothesis == class_size_premise:
    # check if the class size in the hypothesis fully matches the class size in the premise
    label = "entailment"
else:
    # if the hypothesis class size does not contradict the premise one, but also does not fully entail it, we infer neutrality
    label = "neutral"

print(label)
