years_future_premise = 18
years_future_hypothesis = 88

# the hypothesis talks about the number of years in the future, referenced also in the premise
if years_future_hypothesis < years_future_premise:
    # check if the number of years in the future in the hypothesis contradicts the number of years in the future in the premise
    label = "contradiction"
else:
    # if the number of years in the future in the hypothesis does not contradict the number of years in the future in the premise, we can infer entailment
    label = "entailment"

print(label)
