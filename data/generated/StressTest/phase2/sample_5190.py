# Premise: The compound interest earned by Sunil on a certain amount at the end of two years at the rate of 8% p.
# Hypothesis: The compound interest earned by Sunil on a certain amount at the end of two years at the rate of more than 1% p.
# Golden Label: entailment

interest_rate_premise = 8
interest_rate_hypothesis = 1

# the hypothesis talks about the interest rate on a amount, referenced also in the premise
if interest_rate_hypothesis >= interest_rate_premise:
    # check if the hypothesis value contradicts the value of 'interest_rate_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
