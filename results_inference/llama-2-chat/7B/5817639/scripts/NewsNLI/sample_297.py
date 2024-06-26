people_premise = 20
people_hypothesis = 30

# the hypothesis mentions the number of people trapped in the casino, which is also referenced in the premise
if people_hypothesis!= people_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
