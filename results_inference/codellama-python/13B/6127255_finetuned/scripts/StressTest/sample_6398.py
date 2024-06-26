year_premise = 1979
year_hypothesis = 6979
passengers_premise = 32.3
passengers_hypothesis = 32.3
proportion_premise = 1/3
proportion_hypothesis = 1/3

# the hypothesis refers to the same information as the premise, but with a different year
if year_hypothesis!= year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
elif passengers_hypothesis!= passengers_premise:
    # check if the number of passengers in the hypothesis contradicts the number of passengers in the premise
    label = "contradiction"
elif proportion_hypothesis!= proportion_premise:
    # check if the proportion of passengers using the airport in the hypothesis contradicts the proportion in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
