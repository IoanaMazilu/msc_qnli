rajat_vikas_abhishek_ratio_premise = [7, 3, 2]
rajat_vikas_abhishek_ratio_hypothesis = [5, 3, 2]

# the hypothesis refers to the ratio of questions submitted by Rajat, Vikas and Abhishek mentioned in the premise
if rajat_vikas_abhishek_ratio_premise!= rajat_vikas_abhishek_ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
