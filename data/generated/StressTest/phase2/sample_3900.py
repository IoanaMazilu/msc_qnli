# Premise: There are 14 stations between Hyderabad and Bangalore.
# Hypothesis: There are less than 74 stations between Hyderabad and Bangalore.
# Golden Label: entailment

stations_premise = 14
stations_hypothesis = 74

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, referenced also in the premise
if stations_premise >= stations_hypothesis:
    # check if the actual number of stations in the premise contradicts the estimate of less than 'stations_hypothesis'
    label = "contradiction"
else:
    # any number of stations less than 'stations_hypothesis' is consistent with the premise, but since the premise gives an exact number, the hypothesis can be explicitly entailed from the premise
    label = "entailment"

print(label)

