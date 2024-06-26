people_premise = 13

# the hypothesis talks about the number of people in a BCCI meeting, referenced also in the premise
if people_premise < people_premise:
    # check if the hypothesis value contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
