years_premise = 2
years_hypothesis = 6
interest_rate_premise = 4
interest_rate_hypothesis = 4

# the hypothesis talks about the number of years and interest rate, which are also mentioned in the premise
if years_hypothesis!= years_premise:
    # check if the number of years in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
