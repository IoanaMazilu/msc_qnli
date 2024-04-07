# Premise: There are 12 stations between Ernakulam and Chennai.
# Hypothesis: There are more than 12 stations between Ernakulam and Chennai.
# Golden Label: contradiction

stations_premise = 12
stations_hypothesis = 12

# the hypothesis refers to the number of stations between Ernakulam and Chennai mentioned in the premise
if stations_hypothesis != stations_premise:
    # check if the number of stations in the hypothesis contradicts the number of stations stated in the premise
    label = "contradiction"
else:
    # the premise gives an exact number for the stations
    # any number of stations equal to 'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

