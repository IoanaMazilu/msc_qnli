box_caps_premise = 7.0
added_caps_premise = 7.0
total_caps_hypothesis = 14.0

# the hypothesis talks about the total number of bottle caps, which is also referenced in the premise
# compute the total number of bottle caps in the premise
total_caps_premise = box_caps_premise + added_caps_premise
if total_caps_hypothesis!= total_caps_premise:
    # check if the total number of bottle caps from the hypothesis contradicts the total number of bottle caps from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
