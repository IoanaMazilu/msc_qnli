ratio_rajat_vikas_abhishek_premise = 7/3/2
ratio_rajat_vikas_abhishek_hypothesis = 8/3/2

# the hypothesis refers to the ratio of questions submitted by Rajat, Vikas and Abhishek mentioned in the premise
if ratio_rajat_vikas_abhishek_premise >= ratio_rajat_vikas_abhishek_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio of questions submitted in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
