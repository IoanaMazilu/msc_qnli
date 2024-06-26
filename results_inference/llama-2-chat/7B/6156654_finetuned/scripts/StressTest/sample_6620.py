people_selected = 4
people_premise = 7

# the hypothesis refers to the number of people selected, which is also mentioned in the premise
if people_selected >= people_premise:
    # check if the number of people selected in the hypothesis contradicts the number of people selected in the premise
    label = "contradiction"
else:
    # if the number of people selected in the hypothesis is less than the number of people selected in the premise, we can infer entailment
    label = "entailment"

print(label)
