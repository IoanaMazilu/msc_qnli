boys_percentage_premise = 60
boys_percentage_hypothesis = 60

# the hypothesis refers to the percentage of boys at Jones Elementary, also mentioned in the premise
if boys_percentage_hypothesis > boys_percentage_premise:
    # check if the hypothesis percentage contradicts the one given in the premise
    label = "contradiction"
else:
    # the hypothesis does not contradict the premise, but it cannot be explicitly entailed from the premise
    # because the premise and hypothesis are asking a question, not stating a fact
    label = "neutral"

print(label)
