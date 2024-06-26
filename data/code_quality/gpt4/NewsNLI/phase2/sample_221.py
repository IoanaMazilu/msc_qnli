gorillas_premise = 300
gorillas_hypothesis = 300

# the hypothesis mentions the number of endangered mountain gorillas in the park, which is also mentioned in the premise
if gorillas_hypothesis != gorillas_premise:
    # check if the number of gorillas in the hypothesis contradicts the number of gorillas reported in the premise
    label = "contradiction"
else:
    # if the hypothesis number does not contradict the premise number, we can infer entailment
    label = "entailment"

print(label)
