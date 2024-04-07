# Premise: Albert borrowed a total of $5800 from Brian and Charlie.
# Hypothesis: Albert borrowed a total of $less than 8800 from Brian and Charlie.
# Golden Label: entailment

borrowed_premise = 5800
borrowed_hypothesis = 8800

# The hypothesis mentions the total amount borrowed by Albert, which is also referred in the premise
if borrowed_hypothesis <= borrowed_premise:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif borrowed_premise >= borrowed_hypothesis:
    # Check if the premise value contradicts the hypothesis estimate of less than 'borrowed_hypothesis'
    label = "contradiction"
else:
    # If the hypothesis value and the premise value do not contradict each other, we can infer entailment
    label = "entailment"

print(label)

