# Premise: Dan's age after 20 years will be 7 times his age 4 years ago.
# Hypothesis: Dan's age after more than 10 years will be 7 times his age 4 years ago.
# Golden Label: entailment

dan_future_age_factor_premise = 20
dan_past_age_factor_premise = 4
dan_future_age_factor_hypothesis = 10
dan_past_age_factor_hypothesis = 4

# the hypothesis refers to Dan's future age in terms of his past age, just like the premise
if dan_future_age_factor_hypothesis < dan_future_age_factor_premise:
    # check if the time mentioned in the hypothesis contradicts the future time given in the premise
    label = "contradiction"
elif dan_past_age_factor_hypothesis != dan_past_age_factor_premise:
    # check if the past time mentioned in the hypothesis contradicts the past time given in the premise
    label = "contradiction"
else:
    # the hypothesis time does not contradict the premise time, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

