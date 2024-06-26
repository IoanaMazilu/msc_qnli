gomati_rashmi_ratio_premise = 3/5
gomati_rashmi_ratio_hypothesis = 4/5

# the hypothesis refers to the ratio of Gomati's and Rashmi's ages mentioned in the premise
if gomati_rashmi_ratio_hypothesis <= gomati_rashmi_ratio_premise:
    # check if the estimate of 'gomati_rashmi_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio of Gomati's and Rashmi's ages from the hypothesis does not contradict the premise ratio, we can infer entailment
    label = "entailment"

print(label)
