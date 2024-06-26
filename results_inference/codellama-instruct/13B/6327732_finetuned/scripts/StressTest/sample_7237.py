first_day_traveled_premise = 440
first_day_traveled_hypothesis = 240

# the hypothesis refers to the number of miles traveled on the first day of Louisa's vacation
if first_day_traveled_hypothesis >= first_day_traveled_premise:
    # check if the estimate of 'first_day_traveled_hypothesis' contradicts the number of miles traveled in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of miles traveled on the first day of Louisa's vacation
    # any number of miles less than 'first_day_traveled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
