# Premise: John was thrice as old as Tom 6 yrs back.
# Hypothesis: John was thrice as old as Tom less than 8 yrs back.
# Golden Label: entailment

john_age_premise = 6
john_age_hypothesis = 8

# the hypothesis talks about the time when John's age was thrice as Tom's, referenced also in the premise
if john_age_hypothesis > john_age_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif john_age_hypothesis < john_age_premise:
    # check if the hypothesis value is less than the premise value
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

