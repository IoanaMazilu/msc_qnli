# Premise: There are 16 stations between Hyderabad and Bangalore.
# Hypothesis: There are less than 86 stations between Hyderabad and Bangalore.
# Golden Label: entailment

stations_premise = 16
stations_hypothesis = 86

# the hypothesis talks about the number of stations between two cities, referenced also in the premise
if stations_hypothesis <= stations_premise:
    # check if the hypothesis value contradicts the exact number of 'stations_premise'
    label = "contradiction"
elif stations_premise != stations_hypothesis:
    # the premise gives an exact number for the stations
    # any number of stations less than 'stations_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

