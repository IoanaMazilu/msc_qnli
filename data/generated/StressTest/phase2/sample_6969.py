# Premise: There are 8 stations between Vijayawada and Chennai.
# Hypothesis: There are more than 4 stations between Vijayawada and Chennai.
# Golden Label: entailment

stations_premise = 8
stations_hypothesis = 4

# the hypothesis refers to the number of stations between Vijayawada and Chennai mentioned in the premise
if stations_premise <= stations_hypothesis:
    # check if the estimate of 'stations_hypothesis' contradicts the number of stations in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

