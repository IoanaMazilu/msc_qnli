pirates_premise = 6
pirates_hypothesis = 6

# the hypothesis mentions the number of pirates which is also mentioned in the premise
if pirates_hypothesis!= pirates_premise:
    # check if the number of pirates in the hypothesis contradicts the number of pirates reported in the premise
    label = "contradiction"
else:
    # if the number of pirates in the hypothesis does not contradict the number of pirates in the premise, we can infer entailment
    label = "entailment"

print(label)
