ratio_premise = 4/3
ratio_hypothesis = 6/3
future_rahul_age_premise = 34
future_rahul_age_hypothesis = 34

# the hypothesis refers to the ratio between Rahul and Deepak mentioned in the premise
# and the future age of Rahul mentioned in both premise and hypothesis
if ratio_premise <= ratio_hypothesis:
    # check if the estimate of 'ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
elif future_rahul_age_hypothesis!= future_rahul_age_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
