classes_premise = 3
classes_hypothesis = 5

# the hypothesis is about the number of Professor Wang's classes, which is also mentioned in the premise
if classes_premise > classes_hypothesis:
    # check if the number of classes in the premise contradicts the hypothesis
    label = "contradiction"
elif classes_premise < classes_hypothesis:
    # check if the number of classes in the hypothesis contradicts the premise
    label = "entailment"
else:
    # if the number of classes in the premise and the hypothesis are the same, we can infer neutrality
    label = "neutral"

print(label)
