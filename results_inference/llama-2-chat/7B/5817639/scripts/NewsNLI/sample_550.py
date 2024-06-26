width_premise = 0.04
weight_premise = 4000
brightness_premise = 5
brightness_hypothesis = 5

# check if the hypothesis values contradict the premise values
if brightness_hypothesis!= brightness_premise:
    label = "contradiction"
elif width_hypothesis!= width_premise or weight_hypothesis!= weight_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
