year_premise = 1979
year_hypothesis = 1979
passengers_premise = 38.3
passengers_hypothesis = 38.3

# The hypothesis refers to the year and number of passengers mentioned in the premise
if year_hypothesis != year_premise:
    # Check if the year in the hypothesis contradicts the year mentioned in the premise
    label = "contradiction"
elif passengers_hypothesis != passengers_premise:
    # Check if the number of passengers in the hypothesis contradicts the number of passengers reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
