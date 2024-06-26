arrest_chance_premise = 0.40
arrest_chance_hypothesis = 0.40

# the hypothesis mentions the arrest chance for white males, which is also mentioned in the premise
if arrest_chance_hypothesis!= arrest_chance_premise:
    # check if the arrest chance in the hypothesis contradicts the arrest chance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
