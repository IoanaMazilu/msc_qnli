premise_time = 7
hypothesis_time = 6

# the hypothesis refers to the time taken by Henry to run the second leg of the course
if hypothesis_time >= premise_time:
    # check if the estimate of 'hypothesis_time' contradicts the time taken by Henry in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
