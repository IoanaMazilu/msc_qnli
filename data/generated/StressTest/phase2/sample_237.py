# Premise: Alice deposited Rs 2 million in bank at 4% simple interest per year.
# Hypothesis: Alice deposited Rs more than 1 million in bank at 4% simple interest per year.
# Golden Label: entailment

deposit_premise = 2000000
deposit_hypothesis = 1000000
interest_rate_premise = 0.04
interest_rate_hypothesis = 0.04

# the hypothesis refers to the deposit amount and interest rate mentioned in the premise
if deposit_premise <= deposit_hypothesis:
    # check if the estimate of 'deposit_hypothesis' contradicts the deposit amount in the premise
    label = "contradiction"
elif interest_rate_hypothesis != interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

