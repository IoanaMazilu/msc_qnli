train_departure_time_premise = 12
train_departure_time_hypothesis = 12

# the hypothesis talks about the departure time of the train from Chennai to Jammu, which is also mentioned in the premise
if train_departure_time_hypothesis >= train_departure_time_premise:
    # check if the hypothesis value contradicts the premise statement of exactly 'train_departure_time_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than or equal to the premise, it is entailed by the premise
    label = "entailment"

print(label)
