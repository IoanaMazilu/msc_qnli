passengers_premise = 32300000
passengers_hypothesis = 32300000
year_premise = 1979
year_hypothesis = 6979

# the hypothesis refers to the number of airline passengers traveling to or from the United States using Kennedy Airport
# the premise mentions the number of passengers in 1979, but does not provide an exact number
if year_hypothesis < year_premise:
    # check if the hypothesis year is less than the premise year
    label = "contradiction"
elif passengers_hypothesis!= passengers_premise:
    # check if the number of passengers in the hypothesis contradicts the number of passengers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
