tom_goals_premise = 4
tom_goals_hypothesis = 8

# the hypothesis refers to the number of P goals mentioned in the premise
if tom_goals_premise <= tom_goals_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'tom_goals_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of P goals
    # any number of P goals greater than 'tom_goals_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
