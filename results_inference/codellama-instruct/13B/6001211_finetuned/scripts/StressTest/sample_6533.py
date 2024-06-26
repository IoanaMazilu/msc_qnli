year_premise = 1979
year_hypothesis = 7979
passengers_premise = 37.3
passengers_hypothesis = 37.3

# the hypothesis refers to the year and the number of passengers mentioned in the premise
if year_premise!= year_hypothesis:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
elif passengers_premise!= passengers_hypothesis:
    # check if the number of passengers in the hypothesis contradicts the number of passengers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
