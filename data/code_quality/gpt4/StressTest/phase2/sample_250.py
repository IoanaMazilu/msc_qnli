senior_directors_premise = 4
senior_directors_hypothesis = 5
managing_directors_premise = 5
managing_directors_hypothesis = 5

# the hypothesis specifies the number of Senior Managing Directors and Managing Directors at Morgan Goldman, as mentioned in the premise
if senior_directors_hypothesis <= senior_directors_premise:
    # check if the hypothesis value contradicts the estimate of more than 'senior_directors_premise'
    label = "contradiction"
elif managing_directors_hypothesis != managing_directors_premise:
    # check if the number of Managing Directors in the hypothesis contradicts the number of Managing Directors reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of Senior Managing Directors
    # the specified number of Senior Managing Directors in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
