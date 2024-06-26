bonds_denominations_premise = 70
bonds_denominations_hypothesis = 50
bonds_purchased_premise = 10
bonds_purchased_hypothesis = 10

# the hypothesis refers to the number of bonds purchased and the denominations in which they are sold
if bonds_denominations_hypothesis <= bonds_denominations_premise:
    # check if the hypothesis value contradicts the estimate of 'bonds_denominations_premise'
    label = "contradiction"
elif bonds_purchased_hypothesis!= bonds_purchased_premise:
    # check if the number of bonds purchased in the hypothesis contradicts the number of bonds reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
