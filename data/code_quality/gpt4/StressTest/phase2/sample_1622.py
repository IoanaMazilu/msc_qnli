arun_age_future_premise = 26
years_future_premise = 6
arun_age_future_hypothesis = 26
years_future_hypothesis = 8

# the hypothesis compares Arun's future age with the premise
# however, the hypothesis specifies a different number of years in the future
if arun_age_future_premise != arun_age_future_hypothesis or years_future_premise != years_future_hypothesis:
    # check if either the future age or the number of years in the future contradicts the premise
    label = "contradiction"
else:
    # if neither the number of years in the future nor the future age contradicts the premise,
    # we can infer entailment
    label = "entailment"

print(label)
