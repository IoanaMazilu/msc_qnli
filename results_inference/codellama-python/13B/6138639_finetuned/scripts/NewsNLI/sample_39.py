people_premise = 200
people_hypothesis = 200

# the hypothesis mentions the number of people who joined Armstrong in Paisley, which is also referenced in the premise
if people_hypothesis!= people_premise:
    # check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
