total_caps_premise = 7.0
new_caps_premise = 7.0
total_caps_hypothesis = 14.0

# the hypothesis refers to the total number of bottle caps in the box, which is also mentioned in the premise
if total_caps_hypothesis!= total_caps_premise:
    # check if the total number of bottle caps in the hypothesis contradicts the total number of bottle caps in the premise
    label = "contradiction"
elif new_caps_premise!= total_caps_hypothesis:
    # check if the number of new bottle caps in the hypothesis contradicts the number of new bottle caps in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
