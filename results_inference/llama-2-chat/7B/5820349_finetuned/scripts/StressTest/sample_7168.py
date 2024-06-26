people_premise = 1
people_hypothesis = 7

# the hypothesis talks about the number of people who entered the theater between Sujit and Suraj, and after Suraj, both referenced in the premise
if people_hypothesis <= people_premise:
    # check if the hypothesis value contradicts the estimate of more than 'people_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people greater than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
