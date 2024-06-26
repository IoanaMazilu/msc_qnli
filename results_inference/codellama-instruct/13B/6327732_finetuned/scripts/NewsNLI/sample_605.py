deaths_premise = 29
deaths_hypothesis = 35
population_premise = 1599
population_hypothesis = 1599

# the hypothesis mentions the number of deaths in Marion County, which is also mentioned in the premise
# however, the hypothesis mentions a higher number of deaths than the premise
if deaths_hypothesis > deaths_premise:
    # check if the number of deaths in the hypothesis contradicts the number of deaths in the premise
    label = "contradiction"
elif population_hypothesis!= population_premise:
    # check if the population in the hypothesis contradicts the population in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
