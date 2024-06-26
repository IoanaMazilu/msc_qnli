deaths_premise = 1
deaths_hypothesis = 1
injured_premise = 10
injured_hypothesis = 10

# the hypothesis mentions the number of deaths and injured people, which are also mentioned in the premise
if deaths_hypothesis!= deaths_premise:
    # check if the number of deaths in the hypothesis contradicts the number of deaths reported in the premise
    label = "contradiction"
elif injured_hypothesis!= injured_premise:
    # check if the number of injured people from the hypothesis contradicts the number of injured people in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
