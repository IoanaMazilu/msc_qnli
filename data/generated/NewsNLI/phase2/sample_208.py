# Premise: The uncompleted tunnel measures 48 feet in the U.S. and 35 feet in Mexico.
# Hypothesis: 48 feet of tunnel is in United States and 35 feet in Mexico.
# Golden Label: entailment

tunnel_us_premise = 48
tunnel_us_hypothesis = 48
tunnel_mexico_premise = 35
tunnel_mexico_hypothesis = 35

# the hypothesis mentions the length of the tunnel in U.S. and Mexico, which are also mentioned in the premise
if tunnel_us_hypothesis != tunnel_us_premise:
    # check if the length of the tunnel in U.S. in the hypothesis contradicts the length of the tunnel in U.S. reported in the premise
    label = "contradiction"
elif tunnel_mexico_hypothesis != tunnel_mexico_premise:
    # check if the length of the tunnel in Mexico from the hypothesis contradicts the length of the tunnel in Mexico in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

