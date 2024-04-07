# Premise: Tanya is 25% more efficient than Sakshi.
# Hypothesis: Tanya is less than 75% more efficient than Sakshi.
# Golden Label: entailment

efficiency_rate_premise = 25
efficiency_rate_hypothesis = 75

# the hypothesis talks about Tanya's efficiency rate compared to Sakshi, also referenced in the premise
if efficiency_rate_hypothesis < efficiency_rate_premise:
    # check if the hypothesis value contradicts the exact efficiency rate of Tanya in the premise
    label = "contradiction"
elif efficiency_rate_hypothesis == efficiency_rate_premise:
    # if the hypothesis value is equal to the premise value, we can infer entailment
    label = "entailment"
else:
    # the hypothesis value is greater than the premise value but does not contradict it, hence it is neutral
    label = "neutral"

print(label)

