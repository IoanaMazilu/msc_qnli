# Premise: Molly's age in 18 years will be seven times her age six years ago.
# Hypothesis: Molly's age in less than 88 years will be seven times her age six years ago.
# Golden Label: entailment

molly_future_age_premise = 18
molly_future_age_hypothesis = 88
molly_past_age_multiplier = 7

# the hypothesis talks about Molly's age in the future, compared to her age in the past, as mentioned in the premise
if molly_future_age_hypothesis < molly_future_age_premise:
    # check if the hypothesis value contradicts the specific future time stated in the premise
    label = "contradiction"
elif molly_future_age_hypothesis > molly_future_age_premise:
    # the premise gives a specific future time, while the hypothesis gives an estimate (less than a certain time)
    # any future time less than 'molly_future_age_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value and estimate do not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

