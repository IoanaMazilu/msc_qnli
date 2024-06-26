people_entered_theater_premise = 7
people_entered_theater_hypothesis = 8

# the hypothesis refers to the number of people who entered the theater between Sujit and Suraj and after Suraj, mentioned in the premise
if people_entered_theater_premise!= people_entered_theater_hypothesis:
    # check if the number of people who entered the theater in the hypothesis contradicts the number of people who entered the theater in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who entered the theater between Sujit and Suraj
    # any number of people who entered the theater between Sujit and Suraj consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
