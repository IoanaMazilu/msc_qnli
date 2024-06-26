years_premise = 2
years_hypothesis = 2
interest_rate_premise = 4
interest_rate_hypothesis = 4

# the hypothesis refers to the period of time and interest rate mentioned in the premise
if years_hypothesis >= years_premise:
    # check if the hypothesis period of time contradicts the premise period of time
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
