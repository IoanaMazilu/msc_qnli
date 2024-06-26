t_premise = 20
t_hypothesis = 20

# the hypothesis refers to the value of T mentioned in the premise
if t_hypothesis >= (5/9) * (K-32):
    # check if the estimate of 't_hypothesis' contradicts the value of T in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
