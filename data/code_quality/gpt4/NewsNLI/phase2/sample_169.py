projects_value_premise = 36.4
projects_value_hypothesis = 36.4

# the hypothesis mentions the worth of ongoing projects in Libya, which is also mentioned in the premise
if projects_value_hypothesis != projects_value_premise:
    # check if the worth of projects in the hypothesis contradicts the worth of projects reported in the premise
    label = "contradiction"
else:
    # if the worth of projects in the hypothesis does not contradict the value in the premise, we can infer entailment
    label = "entailment"

print(label)
