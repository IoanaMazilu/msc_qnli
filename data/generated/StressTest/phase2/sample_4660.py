# Premise: If total sales of the company X & co is less than 200 cr then, what is sales amount of corporate companies related to banking sector having their head quarters in USA?
# Hypothesis: If total sales of the company X & co is 100 cr then, what is sales amount of corporate companies related to banking sector having their head quarters in USA?
# Golden Label: neutral

total_sales_premise = 200
total_sales_hypothesis = 100

# the hypothesis refers to total sales of the company X & co mentioned in the premise
if total_sales_hypothesis >= total_sales_premise:
    # check if the total sales in the hypothesis contradicts the total sales in the premise
    label = "contradiction"
elif total_sales_hypothesis < total_sales_premise:
    # if the total sales in the hypothesis is less than the total sales in the premise, it can be inferred from the premise
    label = "entailment"
else:
    # otherwise, the relation is neutral
    label = "neutral"

print(label)

