start_caps_premise = 7.0
given_caps_premise = 2.0
end_caps_hypothesis = 4.0

# the hypothesis refers to the number of bottle caps left, which is also mentioned in the premise
# compute the total number of bottle caps given in the premise
total_caps_given_premise = start_caps_premise + given_caps_premise

# check if the number of bottle caps left in the hypothesis contradicts the number of caps given in the premise
if end_caps_hypothesis!= total_caps_given_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
