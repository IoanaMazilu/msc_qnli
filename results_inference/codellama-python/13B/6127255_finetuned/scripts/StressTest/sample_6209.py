flavors_premise = 6
flavors_hypothesis = 1

# the hypothesis talks about the number of ice cream flavors in Preethi's parlor, referenced also in the premise
if flavors_hypothesis!= flavors_premise:
    # check if the number of flavors in the hypothesis contradicts the number of flavors reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
