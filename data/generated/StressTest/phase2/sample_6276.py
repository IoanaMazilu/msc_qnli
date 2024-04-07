# Premise: There are 15 stations between Hyderabad and Bangalore.
# Hypothesis: There are less than 75 stations between Hyderabad and Bangalore.
# Golden Label: entailment

stations_premise = 15
stations_hypothesis = 75

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, which is also referred to in the premise
if stations_premise >= stations_hypothesis:
    # check if the actual number of stations contradicts the hypothesis that there are less than 'stations_hypothesis'
    label = "contradiction"
elif stations_premise == stations_hypothesis:
    # check if the actual number of stations is exactly 'stations_hypothesis'
    label = "contradiction"
else:
    # any number of stations less than 'stations_hypothesis' is consistent with the hypothesis
    # since the premise states an exact number of stations, we can infer entailment
    label = "entailment"

print(label)

