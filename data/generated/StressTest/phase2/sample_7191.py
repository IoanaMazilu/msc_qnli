# Premise: Similarly, there's a train that leaves Chennai bound for Jammu on everyday of the week exactly at 12 noon.
# Hypothesis: Similarly, there's a train that leaves Chennai bound for Jammu on everyday of the week exactly at less than 82 noon.
# Golden Label: entailment

train_departure_time_premise = 12
train_departure_time_hypothesis = 82

# the hypothesis talks about the time a train leaves Chennai, referenced also in the premise
if train_departure_time_hypothesis >= train_departure_time_premise:
    # check if the hypothesis value contradicts the exact departure time in the premise
    label = "contradiction"
elif train_departure_time_hypothesis < train_departure_time_premise:
    # check if the hypothesis value is less than the departure time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

