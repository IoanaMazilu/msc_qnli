premise_suspension = "shortly after his death"
hypothesis_suspension = "after his death"

# extract the numerical information from the premise and hypothesis
premise_time = premise_suspension.split(" ")[0]
hypothesis_time = hypothesis_suspension.split(" ")[0]

# compare the times to determine the label
if premise_time == hypothesis_time:
    label = "entailment"
elif premise_time!= hypothesis_time:
    label = "neutral"
else:
    label = "contradiction"

print(label)
