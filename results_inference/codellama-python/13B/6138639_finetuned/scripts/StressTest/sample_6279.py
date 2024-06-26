ratio_premise = [7, 3, 2]
ratio_hypothesis = [8, 3, 2]

# the hypothesis refers to the ratio of questions submitted by Rajat, Vikas and Abhishek mentioned in the premise
if ratio_hypothesis[0] <= ratio_premise[0]:
    # check if the estimate of 'ratio_hypothesis' contradicts the ratio of questions in the premise
    label = "contradiction"
elif ratio_hypothesis[1]!= ratio_premise[1] or ratio_hypothesis[2]!= ratio_premise[2]:
    # check if the ratio of questions in the hypothesis contradicts the ratio of questions reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
