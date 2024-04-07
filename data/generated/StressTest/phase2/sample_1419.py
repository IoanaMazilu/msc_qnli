# Premise: The compound interest earned by Sunil on a certain amount at the end of two years at the rate of 8% p.
# Hypothesis: The compound interest earned by Sunil on a certain amount at the end of two years at the rate of more than 2% p.
# Golden Label: entailment

interest_rate_premise = 8
interest_rate_hypothesis = 2

# the hypothesis talks about the interest rate, referenced also in the premise
if interest_rate_premise <= interest_rate_hypothesis:
    # check if the interest rate in the premise contradicts the estimate of more than 'interest_rate_hypothesis'
    label = "contradiction"
elif interest_rate_premise > interest_rate_hypothesis:
    # if the interest rate in the premise is greater than the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)

