year_premise = 2979
year_hypothesis = 1979
passengers_premise = 37.3
passengers_hypothesis = 37.3

# the hypothesis refers to the year and the number of passengers mentioned in the premise
if year_hypothesis >= year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
elif passengers_hypothesis!= passengers_premise:
    # check if the number of passengers in the hypothesis contradicts the number of passengers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
