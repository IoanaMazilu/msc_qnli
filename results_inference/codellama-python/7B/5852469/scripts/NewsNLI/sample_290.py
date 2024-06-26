average_deaths_premise = 15000
average_deaths_hypothesis = 15000

# the hypothesis mentions the same information as the premise
if average_deaths_hypothesis!= average_deaths_premise:
    # check if the average number of deaths from the hypothesis contradicts the average number of deaths in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
