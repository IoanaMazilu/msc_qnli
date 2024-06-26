interest_rate_premise = 8
interest_rate_hypothesis = 4

# the hypothesis states a lower interest rate than the premise
if interest_rate_hypothesis > interest_rate_premise:
    label = "contradiction"
elif interest_rate_hypothesis == interest_rate_premise:
    label = "neutral"
else:
    label = "entailment"

print(label)
