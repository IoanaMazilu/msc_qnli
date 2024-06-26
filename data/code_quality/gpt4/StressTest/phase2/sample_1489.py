reading_rate_premise = 7
reading_rate_hypothesis = 1

# the hypothesis refers to the reading rate mentioned in the premise
if reading_rate_hypothesis >= reading_rate_premise:
    # check if the 'reading_rate_hypothesis' contradicts the estimate of less than 'reading_rate_premise'
    label = "contradiction"
elif reading_rate_hypothesis == reading_rate_premise - 1:
    # check if the 'reading_rate_hypothesis' can be fully and explicitly entailed from the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the reading rate
    # any reading rate less than 'reading_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
