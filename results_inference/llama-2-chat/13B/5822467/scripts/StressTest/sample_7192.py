premise_train_time = "less than 82 noon"
hypothesis_train_time = "12 noon"

# extract the time information from the premise and hypothesis
premise_time = datetime.strptime(premise_train_time, "%I %p")  # %I is the hour in 12-hour clock format
hypothesis_time = datetime.strptime(hypothesis_train_time, "%I %p")

# compare the time information
if premise_time == hypothesis_time:
    # the times in the premise and hypothesis match, so we can infer entailment
    label = "entailment"
elif premise_time!= hypothesis_time:
    # the times in the premise and hypothesis do not match, so we can infer contradiction
    label = "contradiction"
else:
    # the premise only gives an estimate of the time, so we cannot infer entailment or contradiction
    label = "neutral"

print(label)
