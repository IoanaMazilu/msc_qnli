 time_premise = 82
time_hypothesis = 12

# the hypothesis talks about the time of departure of a train from Chennai to Jammu, which is also mentioned in the premise
if time_hypothesis >= time_premise:
    # check if the time in the hypothesis contradicts the time given in the premise
    label = "contradiction"
else:
    # if the time in the hypothesis is less than the time in the premise, we can infer entailment
    label = "entailment"

print(label)
