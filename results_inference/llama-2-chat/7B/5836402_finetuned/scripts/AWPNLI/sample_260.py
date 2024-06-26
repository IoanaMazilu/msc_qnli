bought_paper_premise = 900.0
used_paper_premise = 156.0
remaining_paper_hypothesis = 744.0

# the hypothesis refers to the number of remaining paper, which is also mentioned in the premise
# compute the number of remaining paper in the premise
remaining_paper_premise = bought_paper_premise - used_paper_premise
if remaining_paper_hypothesis!= remaining_paper_premise:
    # check if the number of remaining paper in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
