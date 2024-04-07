# Premise: Warner Limited has less than 8 Senior Managing Directors and 6 Managing Directors.
# Hypothesis: Warner Limited has 4 Senior Managing Directors and 6 Managing Directors.
# Golden Label: neutral

senior_directors_premise = 8
senior_directors_hypothesis = 4
directors_premise = 6
directors_hypothesis = 6

# the hypothesis talks about the number of Senior Managing Directors and Managing Directors at Warner Limited, which is also referenced in the premise
if senior_directors_hypothesis >= senior_directors_premise:
    # check if the hypothesis value contradicts the estimate of less than 'senior_directors_premise'
    label = "contradiction"
elif directors_hypothesis != directors_premise:
    # check if the number of Managing Directors in the hypothesis contradicts the number of Managing Directors reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of Senior Managing Directors
    # any number of Senior Managing Directors less than 'senior_directors_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

