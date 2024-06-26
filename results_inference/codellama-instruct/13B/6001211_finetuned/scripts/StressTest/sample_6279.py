rajat_ratio_premise = 7
vikas_ratio_premise = 3
abhishek_ratio_premise = 2

rajat_ratio_hypothesis = 8
vikas_ratio_hypothesis = 3
abhishek_ratio_hypothesis = 2

# the hypothesis refers to the ratio of questions submitted by Rajat, Vikas and Abhishek mentioned in the premise
if rajat_ratio_hypothesis <= rajat_ratio_premise:
    # check if the estimate of 'rajat_ratio_hypothesis' contradicts the ratio of Rajat's questions in the premise
    label = "contradiction"
elif vikas_ratio_hypothesis!= vikas_ratio_premise or abhishek_ratio_hypothesis!= abhishek_ratio_premise:
    # check if the ratio of Vikas' or Abhishek's questions in the hypothesis contradicts the ratio of Vikas' or Abhishek's questions reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
