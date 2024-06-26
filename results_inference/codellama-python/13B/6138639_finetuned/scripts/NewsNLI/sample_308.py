kids_premise = 12000
kids_hypothesis = 12000

# the hypothesis mentions the number of street kids in Jakarta, which is also referenced in the premise
if kids_hypothesis!= kids_premise:
    # check if the number of kids in the hypothesis contradicts the number of kids reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
