t_shirts_returned_premise = 5
t_shirts_returned_hypothesis = 4

# the hypothesis talks about the number of t-shirts returned by Sanoop, which is also mentioned in the premise
if t_shirts_returned_hypothesis >= t_shirts_returned_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
