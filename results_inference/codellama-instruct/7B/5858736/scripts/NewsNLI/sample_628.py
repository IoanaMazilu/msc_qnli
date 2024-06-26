experience_premise = 0
experience_hypothesis = 0

if experience_hypothesis!= experience_premise:
    # check if the military experience in the hypothesis contradicts the experience reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
