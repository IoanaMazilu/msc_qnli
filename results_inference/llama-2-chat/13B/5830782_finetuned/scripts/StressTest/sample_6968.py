property_size_premise = 900
property_size_hypothesis = 400

# the hypothesis refers to the size of the property mentioned in the premise
if property_size_premise!= property_size_hypothesis:
    # check if the size of the property in the hypothesis contradicts the size of the property reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
