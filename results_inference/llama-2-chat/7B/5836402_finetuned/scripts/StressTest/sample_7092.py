ratio_premise = 5/2
ratio_hypothesis = 8/2
future_rahul_age_premise = 26
future_rahul_age_hypothesis = 26

# the hypothesis refers to the ratio between Rahul and Deepak and the future age of Rahul mentioned in the premise
if ratio_premise <= ratio_hypothesis:
    # check if the estimate of 'ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
elif future_rahul_age_hypothesis!= future_rahul_age_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age of Rahul reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
