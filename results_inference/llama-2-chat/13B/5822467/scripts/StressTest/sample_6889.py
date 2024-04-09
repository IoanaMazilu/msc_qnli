premise_ways = 8
hypothesis_ways = 6

# the premise talks about seating less than 8 people, while the hypothesis talks about seating 6 people
if premise_ways <= hypothesis_ways:
    # check if the hypothesis value contradicts the estimate of less than 'premise_ways'
    label = "contradiction"
elif hypothesis_ways!= premise_ways:
    # check if the number of seats in the hypothesis contradicts the number of seats in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
