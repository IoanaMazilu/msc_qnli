year_premise = 1979
year_hypothesis = 6979
passengers_premise = 32.3
passengers_hypothesis = 32.3

# the hypothesis refers to the same number of passengers as the premise, but in a different year
if year_hypothesis >= year_premise:
    # check if the hypothesis year contradicts the premise year
    label = "contradiction"
elif passengers_hypothesis != passengers_premise:
    # check if the number of passengers in the hypothesis contradicts the number of passengers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
