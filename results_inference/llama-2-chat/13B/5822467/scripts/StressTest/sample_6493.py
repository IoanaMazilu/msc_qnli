percentage_premise = 7
percentage_hypothesis = 3
amount_premise = 100

# the premise mentions a percentage of the amount that Dana gives back to her parents each month
if percentage_hypothesis <= percentage_premise:
    # check if the hypothesis value contradicts the estimate of the percentage in the premise
    label = "contradiction"
elif amount_premise - (amount_premise * percentage_hypothesis / 100)!= amount_premise - (amount_premise * percentage_premise / 100):
    # check if the amount of money Dana still owes her parents after four years contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
