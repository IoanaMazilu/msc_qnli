# Premise: If Ashwin paid a total of $125, excluding sales tax, to rent the tool, for how many hours did she rent it?
# Hypothesis: If Ashwin paid a total of $less than 625, excluding sales tax, to rent the tool, for how many hours did she rent it?
# Golden Label: entailment

rent_cost_premise = 125
rent_cost_hypothesis = 625

# The hypothesis talks about the cost Ashwin paid to rent the tool, which is also referenced in the premise
if rent_cost_premise >= rent_cost_hypothesis:
    # check if the value of 'rent_cost_premise' contradicts the estimate of less than 'rent_cost_hypothesis'
    label = "contradiction"
elif rent_cost_hypothesis != rent_cost_premise:
    # check if the cost in the hypothesis contradicts the cost reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

