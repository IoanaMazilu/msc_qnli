ratio_premise = [7, 3, 2]
ratio_hypothesis = [5, 3, 2]

# the hypothesis refers to the ratio of questions submitted by Rajat, Vikas and Abhishek mentioned in the premise
if ratio_premise!= ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratios in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
