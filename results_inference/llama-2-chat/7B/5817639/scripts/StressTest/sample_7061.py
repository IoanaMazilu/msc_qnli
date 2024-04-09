# define variables for the premise and hypothesis
premise_time = 90
hypothesis_time = 80

# check if the hypothesis time contradicts the premise time
if hypothesis_time <= premise_time:
    label = "contradiction"
else:
    # the hypothesis time does not contradict the premise time, so we can infer entailment
    label = "entailment"

print(label)
