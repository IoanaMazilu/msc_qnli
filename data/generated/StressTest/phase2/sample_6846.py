# Premise: The compound interest earned by Sunil on a certain amount at the end of two years at the rate of 8% p.
# Hypothesis: The compound interest earned by Sunil on a certain amount at the end of two years at the rate of more than 7% p.
# Golden Label: entailment

interest_rate_premise = 8
interest_rate_hypothesis = 7

# the hypothesis refers to the interest rate mentioned in the premise
if interest_rate_premise <= interest_rate_hypothesis:
    # check if the 'interest_rate_hypothesis' contradicts the interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

