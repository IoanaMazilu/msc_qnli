ratio_rajat_premise = 7
ratio_vikas_premise = 3
ratio_abhishek_premise = 2

ratio_rajat_hypothesis = 5
ratio_vikas_hypothesis = 3
ratio_abhishek_hypothesis = 2

# the hypothesis refers to the ratio of questions submitted by Rajat, Vikas and Abhishek mentioned in the premise
if ratio_rajat_premise!= ratio_rajat_hypothesis:
    # check if the ratio of questions submitted by Rajat in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
elif ratio_vikas_premise!= ratio_vikas_hypothesis or ratio_abhishek_premise!= ratio_abhishek_hypothesis:
    # check if the ratios of questions submitted by Vikas or Abhishek in the hypothesis contradict the ratios mentioned in the premise
    label = "contradiction"
else:
    # if the ratios in the hypothesis do not contradict the ratios in the premise, we can infer entailment
    label = "entailment"

print(label)
