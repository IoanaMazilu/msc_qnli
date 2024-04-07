# Premise: There are 13 stations between Hyderabad and Bangalore.
# Hypothesis: There are less than 23 stations between Hyderabad and Bangalore.
# Golden Label: entailment

stations_premise = 13
stations_hypothesis = 23

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, referenced also in the premise
if stations_premise >= stations_hypothesis:
    # check if the actual number of stations contradicts the hypothesis of less than 'stations_hypothesis'
    label = "contradiction"
elif stations_premise != stations_hypothesis:
    # check if the number of stations in the premise is different from the 'stations_hypothesis'
    # the premise gives an exact number, any other number would not be explicitly entailed
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

