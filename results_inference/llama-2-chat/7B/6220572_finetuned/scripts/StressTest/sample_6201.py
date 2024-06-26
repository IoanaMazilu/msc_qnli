miles_traveled_premise = 200
miles_traveled_hypothesis = 300

# the hypothesis talks about the number of miles traveled by Louisa on the first day of her vacation, referenced also in the premise
if miles_traveled_hypothesis <= miles_traveled_premise:
    # check if the hypothesis value contradicts the number of miles traveled in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of miles traveled
    # any number of miles less than'miles_traveled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
