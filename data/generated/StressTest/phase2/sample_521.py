# Premise: There are 18 stations between Hyderabad and Bangalore.
# Hypothesis: There are more than 18 stations between Hyderabad and Bangalore.
# Golden Label: contradiction

stations_premise = 18
stations_hypothesis = 18

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, referenced also in the premise
if stations_hypothesis != stations_premise:
    # check if the hypothesis value contradicts the exact number of 'stations_premise'
    label = "contradiction"
else:
    # the hypothesis specifies a number of stations greater than 'stations_premise'
    # this cannot be explicitly entailed from the premise, and it does not contradict the premise either
    label = "neutral"

print(label)

