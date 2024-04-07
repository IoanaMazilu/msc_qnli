# Premise: There are 43 stations between Ernakulam and Chennai.
# Hypothesis: There are less than 73 stations between Ernakulam and Chennai.
# Golden Label: entailment

stations_premise = 43
stations_hypothesis = 73

# the hypothesis refers to the number of stations between Ernakulam and Chennai mentioned in the premise
if stations_premise >= stations_hypothesis:
    # check if the estimate of 'stations_hypothesis' contradicts the number of stations in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

