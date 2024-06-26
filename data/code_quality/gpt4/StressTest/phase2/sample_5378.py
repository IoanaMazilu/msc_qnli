years_premise = 2
years_hypothesis = 3
interest_rate_premise = 4
interest_rate_hypothesis = 4

# the hypothesis talks about the number of years and interest rate which is also referenced in the premise
if years_premise != years_hypothesis:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
elif interest_rate_premise != interest_rate_hypothesis:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
