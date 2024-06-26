protesters_premise = 6
protesters_hypothesis = 6

# the hypothesis mentions the number of protesters and counterprotesters arrested, which is also referenced in the premise
if protesters_hypothesis!= protesters_premise:
    # check if the number of protesters and counterprotesters in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of protesters and counterprotesters in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
