people_entered_premise = 15
people_entered_hypothesis = 20

# the hypothesis refers to the number of people entered the theater before Sujit, mentioned in the premise
if people_entered_premise <= people_entered_hypothesis:
    # check if the estimate of 'people_entered_hypothesis' contradicts the number of people entered the theater in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people entered the theater
    # any number of people greater than 'people_entered_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
