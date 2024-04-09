people_between_premise = 1
people_between_hypothesis = 7
people_after_premise = 20
people_after_hypothesis = 20

# the hypothesis refers to the number of people who entered the theater between Sujit and Suraj and after Suraj, mentioned in the premise
if people_between_hypothesis <= people_between_premise:
    # check if the number of people in the hypothesis contradicts the estimate of more than 'people_between_premise'
    label = "contradiction"
elif people_after_hypothesis!= people_after_premise:
    # check if the number of people after Suraj in the hypothesis contradicts the number of people reported after Suraj in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who entered the theater between Sujit and Suraj
    # any number of people greater than 'people_between_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
