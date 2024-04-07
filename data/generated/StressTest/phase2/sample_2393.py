# Premise: Sanoop bought 8 t-shirts at an average price (arithmetic mean) of Rs.
# Hypothesis: Sanoop bought less than 8 t-shirts at an average price (arithmetic mean) of Rs.
# Golden Label: contradiction

tshirts_bought_premise = 8
tshirts_bought_hypothesis = 8

# the hypothesis refers to the number of t-shirts bought by Sanoop mentioned in the premise
if tshirts_bought_hypothesis >= tshirts_bought_premise:
    # check if the number of t-shirts in the hypothesis contradicts the number of t-shirts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

