people_saturday_premise = people_friday_premise * 3
people_saturday_hypothesis = 416.666666667

if people_saturday_hypothesis!= people_saturday_premise:
    # check if the number of people on Saturday in the hypothesis contradicts the number of people from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)