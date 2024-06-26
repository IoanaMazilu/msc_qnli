rajat_ratio_premise = 7
vikas_ratio_premise = 3
abhishek_ratio_premise = 2

rajat_ratio_hypothesis = 5
vikas_ratio_hypothesis = 3
abhishek_ratio_hypothesis = 2

# the hypothesis refers to the ratio of questions submitted by Rajat, Vikas and Abhishek mentioned in the premise
if rajat_ratio_hypothesis!= rajat_ratio_premise:
    # check if the ratio of questions submitted by Rajat in the hypothesis contradicts the ratio of questions submitted by Rajat in the premise
    label = "contradiction"
elif vikas_ratio_hypothesis!= vikas_ratio_premise or abhishek_ratio_hypothesis!= abhishek_ratio_premise:
    # check if the ratios of questions submitted by Vikas and Abhishek in the hypothesis contradict the ratios of questions submitted by Vikas and Abhishek in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
