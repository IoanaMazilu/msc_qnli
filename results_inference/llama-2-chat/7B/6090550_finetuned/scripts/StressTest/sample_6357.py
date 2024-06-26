ysg=5
ysg_hypothesis=2

# the premise talks about the number of baseball cards given to John
# the hypothesis talks about the number of baseball cards given to John

# the hypothesis refers to the same situation as the premise, but with a different number
if ysg == ysg_hypothesis:
    # check if the number of baseball cards given in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis number does not contradict the premise number, we can infer entailment
    label = "entailment"

print(label)


