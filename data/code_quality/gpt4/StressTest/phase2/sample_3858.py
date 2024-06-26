material1_premise = 2
material1_hypothesis = 8
material2_premise = 0.5
material2_hypothesis = 0.5

# the hypothesis refers to the amount of materials mentioned in the premise
if material1_premise > material1_hypothesis:
    # check if the estimate of 'material1_hypothesis' contradicts the amount of material1 in the premise
    label = "contradiction"
elif material2_hypothesis != material2_premise:
    # check if the amount of material2 in the hypothesis contradicts the amount of material2 reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
