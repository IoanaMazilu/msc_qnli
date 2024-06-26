people_entered_premise = 7
people_entered_hypothesis = 20

# the hypothesis refers to the number of people entering the theater between Sujit and Suraj
if people_entered_premise <= people_entered_hypothesis:
    # check if the estimate of 'people_entered_hypothesis' contradicts the number of people entering the theater between Sujit and Suraj in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people entering the theater between Sujit and Suraj
    # any number of people greater than 'people_entered_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
