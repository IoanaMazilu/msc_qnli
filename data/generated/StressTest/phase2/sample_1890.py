# Premise: There are 10 stations between Trichy and Chennai.
# Hypothesis: There are less than 50 stations between Trichy and Chennai.
# Golden Label: entailment

stations_premise = 10
stations_hypothesis = 50

# the hypothesis refers to the number of stations between Trichy and Chennai mentioned in the premise
if stations_hypothesis < stations_premise:
    # check if the hypothesis value contradicts the number of stations reported in the premise
    label = "contradiction"
elif stations_premise > stations_hypothesis:
    # check if the number of stations in the premise contradicts the estimate of less than 'stations_hypothesis' stations
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

