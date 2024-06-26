people_seating_premise = 8
people_seating_hypothesis = 6

# the hypothesis talks about the number of people that can be seated on a bench, referenced also in the premise
if people_seating_hypothesis >= people_seating_premise:
    # check if the hypothesis value contradicts the estimate of less than 'people_seating_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people less than 'people_seating_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)