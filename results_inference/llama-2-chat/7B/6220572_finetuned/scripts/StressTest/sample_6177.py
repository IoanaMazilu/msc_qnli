ratio_premise = 4/3
ratio_hypothesis = 6/3
rahul_age_premise = 34
rahul_age_hypothesis = 34

# the hypothesis refers to the ratio of Rahul and Deepak and the age of Rahul in the future
if ratio_hypothesis >= ratio_premise:
    # check if the estimate of 'ratio_hypothesis' contradicts the ratio of Rahul and Deepak in the premise
    label = "contradiction"
elif rahul_age_hypothesis!= rahul_age_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age of Rahul reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
