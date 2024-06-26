 protesters_arrested_premise = 6
protesters_arrested_hypothesis = 6

# the hypothesis mentions the number of protesters and counterprotesters arrested, which is also mentioned in the premise
if protesters_arrested_hypothesis!= protesters_arrested_premise:
    # check if the number of arrested protesters in the hypothesis contradicts the number of arrested protesters in the premise
    label = "contradiction"
else:
    # if the number of arrested protesters in the hypothesis does not contradict the number of arrested protesters in the premise, we can infer entailment
    label = "entailment"

print(label)

