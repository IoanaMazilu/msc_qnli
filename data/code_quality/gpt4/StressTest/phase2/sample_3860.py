material1_premise = 2
material1_hypothesis = 2
material2_premise = 0.5
material2_hypothesis = 0.5

# the hypothesis talks about the amount of two types of materials Cheryl needs, referenced also in the premise
if material1_hypothesis != material1_premise:
    # check if the amount of 'material1_hypothesis' contradicts the exact amount of the first type of material in the premise
    label = "contradiction"
elif material2_hypothesis != material2_premise:
    # check if the amount of 'material2_hypothesis' contradicts the exact amount of the second type of material stated in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
