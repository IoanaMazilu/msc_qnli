year_premise = 1979
year_hypothesis = 2979
passengers_premise = 37.3
passengers_hypothesis = 37.3
airport_ratio_premise = 1/3
airport_ratio_hypothesis = 1/3

# the hypothesis refers to the number of passengers and the year mentioned in the premise
if year_hypothesis >= year_premise:
    # check if the year in the hypothesis contradicts the premise
    label = "contradiction"
elif passengers_hypothesis != passengers_premise or airport_ratio_hypothesis != airport_ratio_premise:
    # check if the number of passengers or the airport ratio in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
