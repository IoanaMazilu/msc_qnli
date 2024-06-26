injured_fighters_premise = 30
injured_fighters_hypothesis = 30

# the hypothesis mentions the number of NTC fighters' injuries, which is also referenced in the premise
if injured_fighters_hypothesis!= injured_fighters_premise:
    # check if the number of injured fighters in the hypothesis contradicts the number of injured fighters reported in the premise
    label = "contradiction"
else:
    # if the number of injured fighters in the hypothesis does not contradict the number of injured fighters in the premise, we can infer entailment
    label = "entailment"

print(label)
