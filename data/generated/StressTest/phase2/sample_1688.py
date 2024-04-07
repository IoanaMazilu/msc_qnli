# Premise: There are 17 stations between Hyderabad and Bangalore.
# Hypothesis: There are less than 17 stations between Hyderabad and Bangalore.
# Golden Label: contradiction

stations_premise = 17
stations_hypothesis = 17

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, mentioned also in the premise
if stations_hypothesis >= stations_premise:
    # check if the hypothesis value contradicts the premise of having less than 'stations_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than 'stations_premise', it is entailed by the premise
    label = "entailment"

print(label)

