bonds_sold_denominations_premise = 50 or 100
bonds_sold_denominations_hypothesis = less than 70 or 100

# the hypothesis refers to the denominations of bonds sold, which is also mentioned in the premise
if bonds_sold_denominations_hypothesis <= bonds_sold_denominations_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
