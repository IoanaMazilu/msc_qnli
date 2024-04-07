# Premise: Albert borrowed a total of $more than 1000 from Brian and Milton.
# Hypothesis: Albert borrowed a total of $6000 from Brian and Milton.
# Golden Label: neutral

borrowed_premise = 1000
borrowed_hypothesis = 6000

# The hypothesis refers to the total amount of money borrowed by Albert from Brian and Milton, which is also mentioned in the premise
if borrowed_hypothesis <= borrowed_premise:
    # Check if the value in the hypothesis contradicts the premise's estimate of more than 'borrowed_premise'
    label = "contradiction"
else:
    # The premise gives only a lower limit for the borrowed amount
    # Any amount greater than 'borrowed_premise' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)

