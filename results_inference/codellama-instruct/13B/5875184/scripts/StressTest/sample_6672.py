premise_distance = 100
premise_time_40mph = 1
premise_time_60mph = 3

hypothesis_distance = 100
hypothesis_time_40mph = 5
hypothesis_time_60mph = 3

# the hypothesis refers to the time taken to travel from city A to city B
if hypothesis_time_40mph < premise_time_40mph:
    # check if the hypothesis value contradicts the estimate of less than 'premise_time_40mph'
    label = "contradiction"
elif hypothesis_time_60mph!= premise_time_60mph:
    # check if the number of hours taken to travel at 60 mph in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
