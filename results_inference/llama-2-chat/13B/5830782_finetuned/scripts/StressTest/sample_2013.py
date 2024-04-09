years_premise = 2
years_hypothesis = 6
interest_rate = 4

# the hypothesis refers to the number of years and interest rate mentioned in the premise
if years_premise > years_hypothesis:
    # check if the estimate of 'years_hypothesis' contradicts the number of years in the premise
    label = "contradiction"
elif years_premise < years_hypothesis:
    # if the number of years in the premise is less than the number of years in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the number of years in the premise is equal to the number of years in the hypothesis, we can also infer entailment
    label = "entailment"

print(label)
