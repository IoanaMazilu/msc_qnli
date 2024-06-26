seats_likud_premise = 28
seats_zionist_union_premise = 27
lead_edge_hypothesis = 1

# the hypothesis refers to the slight lead of Netanyahu's party, which is also mentioned in the premise
# however, the hypothesis does not specify the exact number of seats for each party, only the difference between them
if seats_likud_premise - seats_zionist_union_premise != lead_edge_hypothesis:
    # check if the difference in seats from the hypothesis contradicts the difference in seats in the premise
    label = "contradiction"
else:
    # if the difference in seats from the hypothesis does not contradict the difference in seats from the premise, we can infer entailment
    label = "entailment"

print(label)
