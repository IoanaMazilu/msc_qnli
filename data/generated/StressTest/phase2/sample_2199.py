# Premise: There are 28 stations between Hyderabad and Bangalore.
# Hypothesis: There are less than 38 stations between Hyderabad and Bangalore.
# Golden Label: entailment

stations_premise = 28
stations_hypothesis = 38

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, referenced also in the premise
if stations_hypothesis < stations_premise:
    # check if the hypothesis value contradicts the exact number of 'stations_premise'
    label = "contradiction"
elif stations_hypothesis == stations_premise:
    # check if the hypothesis value is exactly equal to the number of 'stations_premise'
    label = "entailment"
else:
    # the premise gives an exact number of stations
    # any number of stations less than 'stations_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

