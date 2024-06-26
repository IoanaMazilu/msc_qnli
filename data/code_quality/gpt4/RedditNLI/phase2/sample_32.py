years_premise = 130
years_hypothesis = 2022-1880

# the hypothesis and premise mention the number of years since young adults lived more with their parents than with partners
if years_hypothesis != years_premise:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
