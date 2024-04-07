# Premise: Albert borrowed a total of $less than 8800 from Brian and Charlie.
# Hypothesis: Albert borrowed a total of $5800 from Brian and Charlie.
# Golden Label: neutral

total_borrowed_premise = 8800
total_borrowed_hypothesis = 5800

# the hypothesis provides a specific amount that Albert borrowed from Brian and Charlie, which is also discussed in the premise
if total_borrowed_hypothesis >= total_borrowed_premise:
    # check if the specific amount in the hypothesis contradicts the estimate of 'less than total_borrowed_premise' in the premise
    label = "contradiction"
else:
    # a specific amount less than 'total_borrowed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

