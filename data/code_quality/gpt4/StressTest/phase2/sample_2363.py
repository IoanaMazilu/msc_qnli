paper_numbers_premise = [12, 24, 36, 48]
paper_numbers_hypothesis = [72, 24, 36, 48]

# the hypothesis talks about the numbers on Jimmy's paper, referenced also in the premise
if paper_numbers_hypothesis != paper_numbers_premise:
    # check if the numbers on the paper in the hypothesis contradicts the numbers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
