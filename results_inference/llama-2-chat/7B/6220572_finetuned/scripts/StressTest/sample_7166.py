people_entered_premise = 15
people_entered_hypothesis = 15

# the hypothesis refers to the number of people entered the theater before Sujit, also mentioned in the premise
if people_entered_hypothesis <= people_entered_premise:
    # check if the hypothesis value contradicts the number of people entered in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people entered
    # any number of people greater than 'people_entered_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
