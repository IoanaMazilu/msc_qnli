# Premise: How much simple interest per annum can I negotiate with my Bank so My Family can pay back in 40 years at most double of the money we will borrow.
# Hypothesis: How much simple interest per annum can I negotiate with my Bank so My Family can pay back in less than 50 years at most double of the money we will borrow.
# Golden Label: entailment

payback_years_premise = 40
payback_years_hypothesis = 50

# the hypothesis refers to the maximum number of years for the payback mentioned in the premise
if payback_years_hypothesis < payback_years_premise:
    # check if the hypothesis value contradicts the maximum number of payback years in the premise
    label = "contradiction"
elif payback_years_hypothesis > payback_years_premise:
    # check if the hypothesis value of 'payback_years_hypothesis' is more than the premise value
    label = "entailment"
else:
    # if the hypothesis value and estimates do not contradict or entail the premise ones, we can infer neutrality
    label = "neutral"

print(label)

