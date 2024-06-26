death_chance_premise = 500
death_chance_hypothesis = 500

# the hypothesis mentions the chance of a woman dying due to domestic abuse if the abuser has access to a gun, which is also mentioned in the premise
if death_chance_hypothesis!= death_chance_premise:
    # check if the death chance in the hypothesis contradicts the death chance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
