# Define the variables for the premise and hypothesis
premise_time_40mph = 1
premise_time_60mph = 3
hypothesis_time_40mph = 5
hypothesis_time_60mph = 3

# The hypothesis refers to the time Andrew drove at 40 mph and 60 mph, which are also mentioned in the premise
if premise_time_40mph >= hypothesis_time_40mph:
    # Check if the time Andrew drove at 40 mph in the premise contradicts the time in the hypothesis
    label = "contradiction"
elif premise_time_60mph!= hypothesis_time_60mph:
    # Check if the time Andrew drove at 60 mph in the premise contradicts the time in the hypothesis
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
