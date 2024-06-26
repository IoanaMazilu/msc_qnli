boys_percentage_premise = 30
boys_percentage_hypothesis = 50

# the hypothesis discusses the percentage of boys at Jones Elementary, also referenced in the premise
if boys_percentage_hypothesis <= boys_percentage_premise:
    # check if the percentage of boys proposed in the hypothesis contradicts the premise's lower bound estimate
    label = "contradiction"
else:
    # the premise proposes a minimum percentage of boys, so any percentage higher than 'boys_percentage_premise' does not contradict the premise,
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
