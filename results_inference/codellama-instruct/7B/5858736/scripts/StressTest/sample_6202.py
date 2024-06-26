traveled_miles_premise = 300
traveled_miles_hypothesis = 200

# the hypothesis talks about the number of miles traveled on the first day of Louisa's vacation
if traveled_miles_hypothesis <= traveled_miles_premise:
    # check if the hypothesis value contradicts the estimate of less than 'traveled_miles_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of miles traveled on the first day of Louisa's vacation
    # any number of miles greater than 'traveled_miles_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
