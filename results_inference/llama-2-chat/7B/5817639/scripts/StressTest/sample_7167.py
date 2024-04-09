people_entered_premise = 7
people_entered_hypothesis = 1

# the hypothesis talks about the number of people who entered the theater between Sujit and Suraj and after Suraj
if people_entered_hypothesis <= people_entered_premise:
    # check if the hypothesis value contradicts the estimate of 'people_entered_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who entered the theater
    # any number of people who entered the theater between Sujit and Suraj and after Suraj is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
