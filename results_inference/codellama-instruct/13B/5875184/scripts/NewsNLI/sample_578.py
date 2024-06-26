premise_peacekeepers = 11800
hypothesis_peacekeepers = 11800

# the hypothesis mentions the number of peacekeepers to be deployed, which is also mentioned in the premise
if hypothesis_peacekeepers!= premise_peacekeepers:
    # check if the number of peacekeepers in the hypothesis contradicts the number of peacekeepers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
