committees_premise = 5
committees_hypothesis = 4
people_premise = 7
people_hypothesis = 7

# the hypothesis refers to the number of people in a committee and the number of committees that can be selected
if committees_hypothesis <= committees_premise:
    # check if the hypothesis value contradicts the number of committees in the premise
    label = "contradiction"
elif people_hypothesis!= people_premise:
    # check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
