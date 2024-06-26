premise_seating_options = 8
hypothesis_seating_options = 6

# the hypothesis refers to the number of people that can be seated on a bench
if hypothesis_seating_options <= premise_seating_options:
    # check if the hypothesis value contradicts the estimate of less than 'premise_seating_options'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people that can be seated on a bench
    # any number of people greater than 'premise_seating_options' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
