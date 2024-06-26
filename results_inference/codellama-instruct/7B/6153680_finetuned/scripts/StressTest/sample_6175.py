x_premise = 55
x_hypothesis = 15

# the hypothesis talks about the time difference between walking and train commute, which is also mentioned in the premise
if x_hypothesis >= x_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
