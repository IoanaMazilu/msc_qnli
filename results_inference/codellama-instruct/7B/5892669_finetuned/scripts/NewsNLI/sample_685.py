people_premise = 155
people_hypothesis = 155

# the hypothesis mentions the number of people aboard, which is also referenced in the premise
if people_hypothesis!= people_premise:
    # check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # if the number of people in the hypothesis does not contradict the number of people in the premise, we can infer entailment
    label = "entailment"

print(label)
