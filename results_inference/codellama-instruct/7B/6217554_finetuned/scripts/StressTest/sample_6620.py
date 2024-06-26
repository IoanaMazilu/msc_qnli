people_premise = 7
people_hypothesis = 7
committee_size = 4

# the hypothesis refers to the number of people from which the committee is to be selected
# the hypothesis gives an estimate for the number of people, which is consistent with the premise
if people_hypothesis >= people_premise:
    # check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
elif committee_size > 4:
    # check if the number of people in the committee contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
