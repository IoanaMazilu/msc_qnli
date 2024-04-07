# Premise: Bhaman travelled for 15 hours.
# Hypothesis: Bhaman travelled for more than 15 hours.
# Golden Label: contradiction

travel_time_premise = 15
travel_time_hypothesis = 15

# the hypothesis talks about the travel time of Bhaman, referenced also in the premise
if travel_time_hypothesis != travel_time_premise:
    # check if the hypothesis value contradicts the exact travel time mentioned in the premise
    label = "contradiction"
else:
    # the premise gives the exact travel time
    # the hypothesis saying that Bhaman travelled for more than 'travel_time_premise' contradicts the premise
    label = "contradiction"

print(label)

