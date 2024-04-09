premise_ passengers = 32300000
premise_year = "less than 6979"
hypothesis_passengers = 32300000
hypothesis_year = "1979"

# convert premise year to integer
premise_year_int = int(premise_year)

# check if hypothesis year is consistent with premise year
if hypothesis_year == premise_year:
    # check if hypothesis passengers is consistent with premise passengers
    if hypothesis_passengers == premise_passengers:
        # entailment
        label = "entailment"
    elif hypothesis_passengers > premise_passengers:
        # contradiction
        label = "contradiction"
    else:
        # neutral
        label = "neutral"
else:
    # if hypothesis year is not consistent with premise year, no comparison can be made
    label = "neutral"

print(label)
