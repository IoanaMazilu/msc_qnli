passengers_premise = 1/3
passengers_hypothesis = 1/3
year_premise = 1979
year_hypothesis = 1979
total_passengers_premise = 37.3
total_passengers_hypothesis = 37.3

# the hypothesis refers to the number of passengers in a given year, referenced also in the premise
if passengers_hypothesis!= passengers_premise:
    # check if the number of passengers in the hypothesis contradicts the number of passengers reported in the premise
    label = "contradiction"
elif year_hypothesis!= year_premise:
    # check if the year in the hypothesis contradicts the year reported in the premise
    label = "contradiction"
elif total_passengers_hypothesis!= total_passengers_premise:
    # check if the total number of passengers in the hypothesis contradicts the total number of passengers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
