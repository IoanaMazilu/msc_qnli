john_age_premise = 3 * tom_age_premise
john_age_hypothesis = 3 * tom_age_hypothesis

# the hypothesis talks about the ratio of John's age to Tom's age in the past, also referenced in the premise
if john_age_hypothesis!= john_age_premise:
    # check if the ratio of John's age in the hypothesis contradicts the ratio of John's age in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of John's age to Tom's age
    # any ratio of John's age to Tom's age consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
