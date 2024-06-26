people_entered_premise = 7
people_entered_hypothesis = 8

# the hypothesis refers to the number of people entered between Sujit and Suraj and after Suraj
if people_entered_hypothesis <= people_entered_premise:
    # check if the estimate of 'people_entered_hypothesis' contradicts the number of people entered in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people entered between Sujit and Suraj
    # any number of people greater than 'people_entered_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
