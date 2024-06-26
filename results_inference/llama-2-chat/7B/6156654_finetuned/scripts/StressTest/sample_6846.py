interest_rate_premise = 8
interest_rate_hypothesis = 7

# the hypothesis refers to the interest rate in the premise
if interest_rate_premise <= interest_rate_hypothesis:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
elif interest_rate_premise > interest_rate_hypothesis:
    # if the interest rate in the hypothesis is greater than the interest rate in the premise, it is consistent
    label = "entailment"
else:
    # if the interest rate in the hypothesis is equal to the interest rate in the premise, it is neutral
    label = "neutral"

print(label)
