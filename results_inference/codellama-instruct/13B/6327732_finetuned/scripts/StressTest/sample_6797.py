deposit_premise = 62500
deposit_hypothesis = 62500
interest_rate_premise = 8
interest_rate_hypothesis = 8
compounding_frequency_premise = "quarterly"
compounding_frequency_hypothesis = "quarterly"

# the hypothesis refers to the amount deposited and the interest rate and compounding frequency mentioned in the premise
if deposit_hypothesis < deposit_premise:
    # check if the estimate of 'deposit_hypothesis' contradicts the amount deposited in the premise
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise or compounding_frequency_hypothesis!= compounding_frequency_premise:
    # check if the interest rate or compounding frequency in the hypothesis contradicts the ones mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
