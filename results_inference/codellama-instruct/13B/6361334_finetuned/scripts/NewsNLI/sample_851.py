# define variables for the entities in the premise and hypothesis
premise_tunnel = "The tunnel split to lead into two separate warehouses in San Diego."
hypothesis_tunnel = "The tunnel was between a Tijuana eat-in kitchen and two San Diego warehouses."

# compare the tunnel entities in the premise and hypothesis
if premise_tunnel!= hypothesis_tunnel:
    # check if the tunnel in the hypothesis contradicts the tunnel in the premise
    label = "contradiction"
else:
    # if the tunnel in the hypothesis does not contradict the tunnel in the premise, we can infer entailment
    label = "entailment"

print(label)
