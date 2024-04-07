# Premise: If total sales of the company X & co is 100 cr then, what is sales amount of corporate companies related to banking sector having their head quarters in USA?
# Hypothesis: If total sales of the company X & co is less than 100 cr then, what is sales amount of corporate companies related to banking sector having their head quarters in USA?
# Golden Label: contradiction

total_sales_premise = 100
total_sales_hypothesis = 100

# the hypothesis refers to the total sales of the company X & co mentioned in the premise
if total_sales_hypothesis < total_sales_premise:
    # check if the total sales in the hypothesis contradicts the total sales reported in the premise
    label = "contradiction"
else:
    # if the total sales in the hypothesis do not contradict the total sales in the premise, we can infer entailment
    label = "entailment"

print(label)

