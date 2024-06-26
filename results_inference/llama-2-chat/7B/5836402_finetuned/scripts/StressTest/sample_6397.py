year_premise = 6979
year_hypothesis = 1979

# the hypothesis refers to the year when the airport usage was approximately 1/3 of the total airline passengers
if year_hypothesis!= year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
