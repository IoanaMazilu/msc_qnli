west_ham_score_premise = 3
west_ham_score_hypothesis = 3

# the hypothesis mentions the number of goals West Ham scored in the second half, which is also referenced in the premise
# however, the hypothesis refers to the final score as 3-3, which contradicts the premise (which states the final score as 3-3)
if west_ham_score_hypothesis!= west_ham_score_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
