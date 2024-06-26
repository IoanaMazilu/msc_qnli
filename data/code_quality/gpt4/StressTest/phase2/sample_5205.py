# age ratio rahul to deepak in the premise
rahul_deepak_ratio_premise = 4 / 3 
# age ratio rahul to deepak in the hypothesis
rahul_deepak_ratio_hypothesis = 7 / 3 

# rahul's age after 4 years in the premise
rahul_age_future_premise = 32 
# rahul's age after 4 years in the hypothesis
rahul_age_future_hypothesis = 32 

# the hypothesis refers to the same age ratio and future age of rahul as mentioned in the premise
if rahul_deepak_ratio_hypothesis <= rahul_deepak_ratio_premise:
    # check if the hypothesis ratio contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if the future age of rahul in the hypothesis contradicts the future age of rahul reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
