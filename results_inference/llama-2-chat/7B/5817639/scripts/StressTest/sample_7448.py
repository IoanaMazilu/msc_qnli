ratio_premise = 4
ratio_hypothesis = 2
age_premise = 26
age_hypothesis = 26

# the hypothesis talks about the ratio and age of two individuals, referenced also in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
elif age_hypothesis!= age_premise:
    # check if the hypothesis age value contradicts the estimate of the age in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
