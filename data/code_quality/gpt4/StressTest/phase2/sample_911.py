payback_years_premise = 40
payback_years_hypothesis = 70

# the hypothesis talks about the number of years to pay back the borrowed money, referenced also in the premise
if payback_years_hypothesis != payback_years_premise:
    # check if the number of years in the hypothesis contradicts the number of years mentioned in the premise
    label = "contradiction"
else:
    # if the number of years in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
