# Premise: There are 10 stations between Hyderabad and Bangalore.
# Hypothesis: There are less than 60 stations between Hyderabad and Bangalore.
# Golden Label: entailment

stations_premise = 10
stations_hypothesis = 60

# the hypothesis mentions the number of stations between Hyderabad and Bangalore, also mentioned in the premise
if stations_premise > stations_hypothesis:
    # check if the number of stations in the premise contradicts the estimate of less than 'stations_hypothesis'
    label = "contradiction"
elif stations_premise < stations_hypothesis:
    # the hypothesis gives an estimate greater than the exact number mentioned in the premise
    # so, it cannot be explicitly entailed from the premise, but it doesn't contradict the premise either
    label = "neutral"
else:
    # if the hypothesis value and the premise value are the same, we can infer entailment
    label = "entailment"

print(label)

