people_entered_premise = 1
people_entered_hypothesis = 7
people_entered_after_suraj_premise = 20
people_entered_after_suraj_hypothesis = 20

# the hypothesis refers to the number of people who entered the theater between Sujit and Suraj and after Suraj, mentioned in the premise
if people_entered_hypothesis <= people_entered_premise:
    # check if the number of people in the hypothesis contradicts the estimate of more than 'people_entered_premise'
    label = "contradiction"
elif people_entered_after_suraj_hypothesis!= people_entered_after_suraj_premise:
    # check if the number of people after Suraj in the hypothesis contradicts the number of people after Suraj reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who entered the theater between Sujit and Suraj
    # any number of people greater than 'people_entered_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
