passengers_premise = 32.3e6
passengers_hypothesis = 32.3e6
year_premise = 1979
year_hypothesis = 6979

# the hypothesis refers to the number of passengers and the year, which are also mentioned in the premise
if passengers_hypothesis!= passengers_premise:
    # check if the number of passengers in the hypothesis contradicts the number of passengers reported in the premise
    label = "contradiction"
elif year_hypothesis!= year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
