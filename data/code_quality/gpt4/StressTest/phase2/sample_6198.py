stations_premise = 18
stations_hypothesis = 48

# the hypothesis talks about the number of stations between two cities, referenced also in the premise
if stations_premise >= stations_hypothesis:
    # check if the premise value contradicts the estimate of less than 'stations_hypothesis'
    label = "contradiction"
elif stations_premise != stations_hypothesis:
    # any number of stations less than 'stations_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "neutral"
else:
    # if the premise value does not contradict the hypothesis and can be explicitly entailed from the hypothesis
    label = "entailment"

print(label)
