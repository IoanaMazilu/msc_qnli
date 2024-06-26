t_shirts_returned_premise = 4
t_shirts_returned_hypothesis = 5

# the hypothesis talks about the number of t-shirts returned by Sanoop, which is also mentioned in the premise
if t_shirts_returned_hypothesis >= t_shirts_returned_premise:
    # check if the hypothesis value contradicts the premise statement of 't_shirts_returned_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than or equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
