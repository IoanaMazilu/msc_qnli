miles_traveled_premise = 300
miles_traveled_hypothesis = 100

# the hypothesis talks about the miles traveled by Louisa on the first day of vacation, which is also referenced in the premise
if miles_traveled_hypothesis >= miles_traveled_premise:
    # check if the hypothesis value contradicts the estimate of less than 'miles_traveled_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the miles traveled
    # any miles traveled less than 'miles_traveled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
