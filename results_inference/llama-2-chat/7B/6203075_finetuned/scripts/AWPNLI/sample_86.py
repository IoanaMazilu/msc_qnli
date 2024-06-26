bottle_caps_premise = 7.0
bottle_caps_added = 7.0
total_bottle_caps_hypothesis = 14.0

# the hypothesis refers to the total number of bottle caps in the box, which is also mentioned in the premise
# compute the total number of bottle caps in the premise
total_bottle_caps_premise = bottle_caps_premise + bottle_caps_added
if total_bottle_caps_hypothesis!= total_bottle_caps_premise:
    # check if the number of bottle caps in the hypothesis contradicts the number of bottle caps from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)