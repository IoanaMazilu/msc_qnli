year_premise = 1979
year_hypothesis = 5979
passengers_premise = 38.3
passengers_hypothesis = 38.3

# the hypothesis refers to the year and number of passengers mentioned in the premise
if year_hypothesis >= year_premise:
    # check if the year in the hypothesis contradicts the year mentioned in the premise
    label = "contradiction"
elif passengers_premise != passengers_hypothesis:
    # check if the number of passengers in the hypothesis contradicts the number of passengers mentioned in the premise
    label = "contradiction"
else:
    # if the year and number of passengers in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)
