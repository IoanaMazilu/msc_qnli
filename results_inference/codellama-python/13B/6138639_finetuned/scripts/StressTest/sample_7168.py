people_entered_premise = 1
people_entered_hypothesis = 7

# the hypothesis talks about the number of people who entered the theater between Sujit and Suraj, referenced also in the premise
if people_entered_hypothesis <= people_entered_premise:
    # check if the hypothesis value contradicts the estimate of more than 'people_entered_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people greater than 'people_entered_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
