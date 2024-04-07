# Premise: If Rahul paid a total of $160, excluding sales tax, to rent the tool, for how many hours did she rent it?
# Hypothesis: If Rahul paid a total of $less than 360, excluding sales tax, to rent the tool, for how many hours did she rent it?
# Golden Label: entailment

rental_cost_premise = 160
rental_cost_hypothesis = 360

# the hypothesis talks about the rental cost paid by Rahul, referenced also in the premise
if rental_cost_hypothesis <= rental_cost_premise:
    # check if the hypothesis value contradicts the estimate of 'rental_cost_premise'
    label = "contradiction"
else:
    # since the hypothesis proposes a value larger than the one in the premise
    # this can be considered neutral as it does not contradict, but also cannot be fully entailed from the premise
    label = "neutral"

print(label)

