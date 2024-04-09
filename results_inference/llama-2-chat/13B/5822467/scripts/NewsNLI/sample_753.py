pressure_premise = 0.5
goals_premise = 2

# define variables for the hypothesis
juan_mata_hypothesis = 1
frank_lampard_hypothesis = 1

# extract numerical values from the premise and hypothesis
pressure_hypothesis = float(juan_mata_hypothesis + frank_lampard_hypothesis)

# compare the pressure in the premise and hypothesis
if pressure_hypothesis > pressure_premise:
    # the hypothesis mentions more pressure than the premise, so the label is contradiction
    label = "contradiction"
elif pressure_hypothesis < pressure_premise:
    # the hypothesis mentions less pressure than the premise, so the label is entailment
    label = "entailment"
else:
    # if the pressure in the hypothesis is the same as the premise, the label is neutral
    label = "neutral"

# compare the number of goals in the premise and hypothesis
if goals_hypothesis!= goals_premise:
    # the hypothesis mentions a different number of goals than the premise, so the label is contradiction
    label = "contradiction"

print(label)
