train_departure_premise = 12
train_departure_hypothesis = 62

# the hypothesis refers to the time of departure of a train from Jammu to Chennai, mentioned in the premise
if train_departure_premise!= train_departure_hypothesis:
    # check if the departure time in the hypothesis contradicts the departure time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
