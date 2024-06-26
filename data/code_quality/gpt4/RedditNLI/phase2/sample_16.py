paper_number_premise = 2004
paper_number_hypothesis = 2001

# the hypothesis and premise mention the number of a working paper published by the ECB
if paper_number_hypothesis != paper_number_premise:
    # check if the number of the working paper in the hypothesis contradicts the number of the working paper in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
