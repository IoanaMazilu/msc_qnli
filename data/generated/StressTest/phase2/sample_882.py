# Premise: There are 28 stations between Ernakulam and Chennai.
# Hypothesis: There are less than 58 stations between Ernakulam and Chennai.
# Golden Label: entailment

stations_premise = 28
stations_hypothesis = 58

# the hypothesis refers to the number of stations between Ernakulam and Chennai mentioned in the premise
if stations_premise >= stations_hypothesis:
    # check if the number of stations in the premise contradicts the estimate of less than 'stations_hypothesis'
    label = "contradiction"
else:
    # if the number of stations in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
