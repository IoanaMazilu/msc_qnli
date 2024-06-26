y - 95
x - 85

# the premise mentions giving exactly 95 $ to John
# the hypothesis mentions giving more than 85 $ to John

if x!= y:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis amount does not contradict the premise amount
    # then it can be entailed from the premise
    label = "entailment"

print(label)
