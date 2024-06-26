deaths_premise = 3
deaths_hypothesis = 3

# the hypothesis mentions the number of people who have died in Minnesota, which is also mentioned in the premise
if deaths_hypothesis > deaths_premise:
    # check if the number of deaths in the hypothesis contradicts the number of deaths reported in the premise
    label = "contradiction"
elif deaths_hypothesis < deaths_premise:
    # check if the number of deaths in the hypothesis is less than the number of deaths reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
