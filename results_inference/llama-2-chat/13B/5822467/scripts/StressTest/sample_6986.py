pen_count_premise = 12
pen_count_hypothesis = float(input("Enter the number of pens purchased: "))
pen_cost_premise = 42.00

# the hypothesis refers to the number of pens purchased and the cost
if pen_count_hypothesis > pen_count_premise:
    # check if the hypothesis value contradicts the estimate of 'pen_count_premise'
    label = "contradiction"
elif pen_cost_premise!= pen_cost_hypothesis:
    # check if the cost of the pens in the hypothesis contradicts the cost reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
