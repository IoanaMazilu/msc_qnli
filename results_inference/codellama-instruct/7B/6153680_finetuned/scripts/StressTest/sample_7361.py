boys_14_premise = 80
boys_15_premise = 70
boys_13_premise = 50
boys_12_premise = 60

boys_14_hypothesis = 50
boys_15_hypothesis = 70
boys_13_hypothesis = 50
boys_12_hypothesis = 60

# the hypothesis refers to the number of boys in each age group mentioned in the premise
if boys_14_hypothesis!= boys_14_premise:
    # check if the number of boys in age group 14 in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif boys_15_hypothesis!= boys_15_premise:
    # check if the number of boys in age group 15 in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif boys_13_hypothesis!= boys_13_premise:
    # check if the number of boys in age group 13 in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif boys_12_hypothesis!= boys_12_premise:
    # check if the number of boys in age group 12 in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
