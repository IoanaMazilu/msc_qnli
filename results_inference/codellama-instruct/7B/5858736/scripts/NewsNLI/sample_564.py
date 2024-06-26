# Define variables for the premise and hypothesis
poll_size = 1005
percentage_never_redeem = 0.4

# Extract the numerical information from the premise
poll_size_premise = 1005
percentage_never_redeem_premise = 0.4

# Extract the numerical information from the hypothesis
poll_size_hypothesis = 1005
percentage_never_redeem_hypothesis = 0.4

# Check if the hypothesis values and estimates do not contradict the premise values
if percentage_never_redeem_hypothesis!= percentage_never_redeem_premise:
    # The hypothesis mentions a different percentage of passengers who never redeem loyalty miles, which contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
