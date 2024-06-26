pat_stops_premise = 30
pat_stops_hypothesis = 50

# the hypothesis refers to the moment Pat stops to stretch, mentioned in the premise
if pat_stops_premise >= pat_stops_hypothesis:
    # check if the time when Pat stops as per the premise contradicts the hypothesis
    label = "contradiction"
elif pat_stops_premise == pat_stops_hypothesis:
    # if the time when Pat stops as per the premise equals the time in the hypothesis
    label = "entailment"
else:
    # the premise gives a specific time when Pat stops
    # any time less than 'pat_stops_hypothesis' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)
