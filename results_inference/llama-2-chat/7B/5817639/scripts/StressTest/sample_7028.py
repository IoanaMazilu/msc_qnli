# define variables for the premise and hypothesis
premise_time = 120
hypothesis_time = 150

# check if the hypothesis time contradicts the premise time
if hypothesis_time > premise_time:
    label = "contradiction"
elif hypothesis_time == premise_time:
    # if the hypothesis time is equal to the premise time, it cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # the premise gives only an estimate for the time, any time greater than 'premise_time' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)
