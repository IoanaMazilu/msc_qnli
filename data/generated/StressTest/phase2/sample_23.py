# Premise: There are 32 stations between Ernakulam and Chennai.
# Hypothesis: There are less than 32 stations between Ernakulam and Chennai.
# Golden Label: contradiction

stations_premise = 32
stations_hypothesis = 32

# the hypothesis talks about the number of stations between two places, which is also mentioned in the premise
if stations_hypothesis < stations_premise:
    # the hypothesis says there are less than 'stations_premise' stations, which is consistent with the premise
    label = "entailment"
elif stations_hypothesis > stations_premise:
    # check if the hypothesis contradicts the statement of 'stations_premise' stations in the premise
    label = "contradiction"
else:
    # the premise states exactly 'stations_premise' stations, so any other number of stations would be neutral
    label = "neutral"

print(label)

