year_premise = 1979
year_hypothesis = 6979

# the hypothesis talks about the year of the airline passengers mentioned in the premise
if year_hypothesis!= year_premise:
    # check if the year in the hypothesis contradicts the year reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
