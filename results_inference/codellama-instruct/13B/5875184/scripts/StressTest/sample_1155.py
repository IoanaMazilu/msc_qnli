premise_year = 1979
hypothesis_year = 2979
premise_passengers = 37300000
hypothesis_passengers = 37300000

# the hypothesis refers to a year after the premise year
if hypothesis_year <= premise_year:
    # check if the hypothesis value contradicts the estimate of 'premise_passengers'
    label = "contradiction"
elif hypothesis_passengers!= premise_passengers:
    # check if the number of passengers in the hypothesis contradicts the number of passengers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
