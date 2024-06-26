stretch_time_pat_premise = 20
stretch_time_pat_hypothesis = 80

# the hypothesis refers to the time it takes for Pat to stretch, also mentioned in the premise
if stretch_time_pat_hypothesis!= stretch_time_pat_premise:
    # check if the time it takes for Pat to stretch in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
