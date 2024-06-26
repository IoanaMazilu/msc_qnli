stations_between_premise = 28
stations_between_hypothesis = 28

# the hypothesis and premise both refer to the number of stations between Hyderabad and Bangalore
if stations_between_hypothesis < stations_between_premise:
    # check if 'stations_between_hypothesis' is less than 'stations_between_premise'
    label = "entailment"
elif stations_between_hypothesis == stations_between_premise:
    # check if 'stations_between_hypothesis' contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict or entail from the premise, it is neutral
    label = "neutral"

print(label)
