# Premise: Albert borrowed a total of $5700 from Brian and Charlie.
# Hypothesis: Albert borrowed a total of $less than 8700 from Brian and Charlie.
# Golden Label: entailment

borrowed_premise = 5700
borrowed_hypothesis = 8700

# the hypothesis talks about the total amount Albert borrowed from Brian and Charlie, also mentioned in the premise
if borrowed_hypothesis < borrowed_premise:
    # check if the hypothesis value contradicts the total amount Albert borrowed from Brian and Charlie in the premise
    label = "contradiction"
elif borrowed_hypothesis == borrowed_premise:
    # check if the amount borrowed in the hypothesis equals that in the premise
    label = "entailment"
else:
    # the premise gives a specific amount Albert borrowed
    # any amount less than 'borrowed_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

