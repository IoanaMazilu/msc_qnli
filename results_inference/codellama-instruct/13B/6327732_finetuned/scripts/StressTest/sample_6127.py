premise_people = 41
hypothesis_people = 31

# the hypothesis refers to the number of people who have visited both Iceland and Norway
if hypothesis_people >= premise_people:
    # check if the hypothesis value contradicts the estimate of less than 'premise_people'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who have visited both Iceland and Norway
    # any number of people less than 'premise_people' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
