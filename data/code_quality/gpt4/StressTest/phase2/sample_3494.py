arun_age_future_premise = 25
arun_age_future_hypothesis = 25
years_in_future_premise = 5
years_in_future_hypothesis = 7

# the hypothesis refers to Arun's future age and the number of years from now, mentioned in the premise
if arun_age_future_hypothesis != arun_age_future_premise:
    # check if the future age in the hypothesis contradicts the future age stated in the premise
    label = "contradiction"
elif years_in_future_hypothesis != years_in_future_premise:
    # check if the number of years in the future stated in the hypothesis contradicts the number of years in the future stated in the premise
    label = "contradiction"
else:
    # if the future age and the number of years in the future in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)
