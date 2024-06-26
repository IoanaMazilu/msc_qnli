firewood_per_sack = 20.0
filled_sacks = 6.0
total_wood_gathered = 80.0

# the hypothesis talks about the number of filled sacks, which is also mentioned in the premise
if filled_sacks >= total_wood_gathered:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
