passengers_premise = 32.3e6
passengers_hypothesis = 32.3e6
year_premise = 1979
year_hypothesis = 6979

# the hypothesis refers to the number of passengers and the year, both mentioned in the premise
if passengers_hypothesis <= passengers_premise:
    # check if the hypothesis value contradicts the estimate of more than 'passengers_premise'
    label = "contradiction"
elif year_hypothesis < year_premise:
    # check if the hypothesis year contradicts the premise year
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
