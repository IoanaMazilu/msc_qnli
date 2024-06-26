deaths_premise = 800
deaths_hypothesis = 800
infected_premise = 16000
infected_hypothesis = 16000

# the hypothesis mentions the number of deaths and infected people, which are also mentioned in the premise
if deaths_hypothesis!= deaths_premise:
    # check if the number of deaths in the hypothesis contradicts the number of deaths in the premise
    label = "contradiction"
elif infected_hypothesis!= infected_premise:
    # check if the number of infected people in the hypothesis contradicts the number of infected people in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
