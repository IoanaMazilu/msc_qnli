# Premise: Jacob's age 18 years hence will be thrice his age four years ago.
# Hypothesis: Jacob's age less than 28 years hence will be thrice his age four years ago.
# Golden Label: entailment

age_future_premise = 18
age_future_hypothesis = 28
age_past = 4

# the hypothesis talks about Jacob's age in the future, referenced also in the premise
if age_future_hypothesis >= age_future_premise:
    # check if the hypothesis value contradicts the estimate of less than 'age_future_hypothesis'
    label = "contradiction"
else:
    # the premise gives a specific age for Jacob in the future
    # any age less than 'age_future_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

