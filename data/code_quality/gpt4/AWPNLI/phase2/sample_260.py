bought_paper_premise = 900.0
used_paper_premise = 156.0
left_paper_hypothesis = 744.0

# the hypothesis refers to the number of paper left, which can be computed from the premise
# compute the total number of paper left in the premise
left_paper_premise = bought_paper_premise - used_paper_premise
if left_paper_hypothesis != left_paper_premise:
    # check if the number of paper left in the hypothesis contradicts the number of paper left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
