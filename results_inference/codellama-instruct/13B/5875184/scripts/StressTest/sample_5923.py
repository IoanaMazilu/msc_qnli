premise = "If the trip home took less than 3/2 hour longer than the trip to the beach, how many kilometers o did Carl drive each way?"
hypothesis = "If the trip home took 1/2 hour longer than the trip to the beach, how many kilometers o did Carl drive each way?"

# extract the numerical entities from the premise and hypothesis
premise_time = premise.split(" ")[-1]
hypothesis_time = hypothesis.split(" ")[-1]

# check if the hypothesis time is less than the premise time
if hypothesis_time < premise_time:
    # check if the hypothesis time is 1/2 hour longer than the premise time
    if hypothesis_time + 0.5 == premise_time:
        # the hypothesis is consistent with the premise, but cannot be explicitly entailed from it
        label = "neutral"
    else:
        # the hypothesis contradicts the premise
        label = "contradiction"
else:
    # the hypothesis is not less than the premise time, so it cannot be consistent with the premise
    label = "contradiction"

print(label)
