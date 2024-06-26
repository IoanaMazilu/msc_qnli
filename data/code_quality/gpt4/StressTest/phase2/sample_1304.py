reading_rate_premise = 5 # pages per 5 minutes
reading_rate_hypothesis = 5 # pages per 5 minutes
# the hypothesis states a different reading rate than the one in the premise

if reading_rate_hypothesis < reading_rate_premise:
    # the hypothesis value is less than the premise one, which is consistent with the hypothesis statement
    label = "entailment"
elif reading_rate_hypothesis >= reading_rate_premise:
    # the hypothesis value contradicts the estimate from the premise
    label = "contradiction"
else:
    # any reading rate less than 'reading_rate_premise' does not contradict the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)