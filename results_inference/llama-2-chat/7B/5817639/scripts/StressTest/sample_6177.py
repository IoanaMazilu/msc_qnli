ratio_premise = 4
ratio_hypothesis = 6
age_premise = 34
age_hypothesis = 34

# the hypothesis talks about the ratio between two individuals and their age after 6 years
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
elif age_hypothesis!= age_premise:
    # check if the estimated age of Rahul in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
