floor_premise = 51
floor_hypothesis = 81
rate_premise = 63
rate_hypothesis = 63

# the hypothesis talks about the floor number and the rate of the elevator mentioned in the premise
if floor_hypothesis!= floor_premise:
    # check if the floor number in the hypothesis contradicts the floor number reported in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate of the elevator in the hypothesis contradicts the rate of the elevator reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
