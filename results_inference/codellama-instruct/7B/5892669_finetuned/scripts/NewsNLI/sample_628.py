experience_premise = 0
experience_hypothesis = 0

# the hypothesis mentions the military's zero experience in managing the country politically, which is also referenced in the premise
if experience_hypothesis!= experience_premise:
    # check if the experience in the hypothesis contradicts the experience reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
