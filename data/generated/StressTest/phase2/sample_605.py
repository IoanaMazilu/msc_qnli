# Premise: Bhavan travelled for 20 hours.
# Hypothesis: Bhavan travelled for less than 20 hours.
# Golden Label: contradiction

travel_time_premise = 20
travel_time_hypothesis = 20

# the hypothesis talks about the travel duration of Bhavan, which has also been mentioned in the premise
if travel_time_hypothesis >= travel_time_premise:
    # check if the hypothesis value contradicts the premise value of 'travel_time_premise'
    label = "contradiction"
else:
    # the premise gives the exact travel time for Bhavan
    # any travel time less than 'travel_time_premise' contradicts the premise
    label = "entailment"

print(label)

