helicopters_premise = 2
helicopters_hypothesis = 2

# the hypothesis mentions the number of helicopters from the opposition, which is also referenced in the premise
# however, the premise mentions that the helicopters were flown from Tobruk to join the fight in Ajdabiya, not necessarily to attack
# thus, we cannot fully entail the attacking action from the premise
if helicopters_hypothesis != helicopters_premise:
    # check if the number of helicopters in the hypothesis contradicts the number of helicopters mentioned in the premise
    label = "contradiction"
else:
    # if the number of helicopters does not contradict, we infer neutrality as the action cannot be fully entailed
    label = "neutral"

print(label)
