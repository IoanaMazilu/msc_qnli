ratio_premise = 6/3
ratio_hypothesis = 4/3
age_premise = 34
age_hypothesis = 34

# the hypothesis refers to the ratio between Rahul and Deepak, which is also mentioned in the premise
if ratio_premise <= ratio_hypothesis:
    # check if the estimate of 'ratio_hypothesis' contradicts the ratio mentioned in the premise
    label = "contradiction"
elif age_hypothesis!= age_premise:
    # check if the age mentioned in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
