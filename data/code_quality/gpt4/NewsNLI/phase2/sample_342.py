possible_dead_premise = 300
possible_dead_hypothesis = 300

# the hypothesis mentions the number of feared dead people, which is also mentioned in the premise
if possible_dead_hypothesis != possible_dead_premise:
    # check if the number of feared dead people in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
