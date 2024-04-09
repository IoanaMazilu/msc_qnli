ratio_premise = 7/3
ratio_hypothesis = 8/3

# the hypothesis refers to the ratio of questions submitted by Rajat, Vikas and Abhishek mentioned in the premise
if ratio_premise >= ratio_hypothesis:
    # check if the estimate of 'ratio_hypothesis' contradicts the ratio of question submissions in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
