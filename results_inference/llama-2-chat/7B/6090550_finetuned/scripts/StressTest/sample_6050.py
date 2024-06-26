y = 95
x = 55

# the hypothesis talks about the amount of money that the speaker wants to give to John
# the premise talks about the same amount of money that the speaker wants to give to John

if y!= x:
    # check if the amount of money in the hypothesis contradicts the amount of money in the premise
    label = "contradiction"
else:
    # if the amount of money in the hypothesis does not contradict the amount of money in the premise, we can infer entailment
    label = "entailment"

print(label)
