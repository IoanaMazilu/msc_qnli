# Define the variables for the premise and hypothesis
premise_time_40mph = 5
premise_time_60mph = 3
hypothesis_time_40mph = 1
hypothesis_time_60mph = 3

# The hypothesis refers to the time Andrew spent driving at different speeds, which are also mentioned in the premise
if hypothesis_time_40mph >= premise_time_40mph:
    # Check if the time Andrew spent driving at 40 mph in the hypothesis contradicts the premise
    label = "contradiction"
elif hypothesis_time_60mph!= premise_time_60mph:
    # Check if the time Andrew spent driving at 60 mph in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
