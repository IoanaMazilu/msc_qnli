# Premise: If Jadeja paid a total of $less than 533, excluding sales tax, to rent the tool, for how many hours did she rent it?
# Hypothesis: If Jadeja paid a total of $133, excluding sales tax, to rent the tool, for how many hours did she rent it?
# Golden Label: neutral

rent_cost_premise = 533
rent_cost_hypothesis = 133

# the hypothesis talks about the cost of renting a tool, mentioned in the premise
if rent_cost_hypothesis >= rent_cost_premise:
    # check if the hypothesis value contradicts the estimate of less than 'rent_cost_premise'
    label = "contradiction"
elif rent_cost_hypothesis < rent_cost_premise:
    # the premise gives only an estimate for the cost of renting
    # any cost of renting less than 'rent_cost_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

