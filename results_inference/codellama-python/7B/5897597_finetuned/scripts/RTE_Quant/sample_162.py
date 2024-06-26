pills_premise = 200
pills_hypothesis = 200
total_pills_premise = 70e6
total_pills_hypothesis = 70e6

# the hypothesis talks about the number of pills with metal detected, which is also mentioned in the premise
if pills_hypothesis!= pills_premise:
    # check if the number of pills with metal detected in the hypothesis contradicts the number of pills from the premise
    label = "contradiction"
elif total_pills_hypothesis!= total_pills_premise:
    # check if the total number of pills in the hypothesis contradicts the total number of pills in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
