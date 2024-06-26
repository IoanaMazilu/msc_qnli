deaths_premise = 4
wounded_premise = 80
deaths_hypothesis = 4
wounded_hypothesis = 80

# the hypothesis talks about the number of deaths and wounded in a mortar attack north of Baghdad, which is also mentioned in the premise
if deaths_hypothesis!= deaths_premise:
    # check if the number of deaths in the hypothesis contradicts the number of deaths from the premise
    label = "contradiction"
elif wounded_hypothesis!= wounded_premise:
    # check if the number of wounded in the hypothesis contradicts the number of wounded from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
