crimes_premise = 12
crimes_hypothesis = 12

# the hypothesis mentions the number of potentially linked crimes that officers are investigating, which is also referenced in the premise
if crimes_hypothesis != crimes_premise:
    # check if the number of crimes in the hypothesis contradicts the number of crimes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
