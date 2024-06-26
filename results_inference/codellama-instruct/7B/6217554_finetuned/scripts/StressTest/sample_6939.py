floor_Jose_premise = 51
floor_Jose_hypothesis = 61
rate_Jose_premise = 63
rate_Jose_hypothesis = 63

# the hypothesis talks about the floor where Jose gets on the elevator and the rate of the elevator
if floor_Jose_hypothesis >= floor_Jose_premise:
    # check if the floor where Jose gets on the elevator in the hypothesis contradicts the floor reported in the premise
    label = "contradiction"
elif rate_Jose_hypothesis!= rate_Jose_premise:
    # check if the rate of the elevator in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
