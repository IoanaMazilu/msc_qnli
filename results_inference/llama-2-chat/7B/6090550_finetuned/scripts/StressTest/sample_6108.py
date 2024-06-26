sales_staff_premise_level_1 = 15
sales_staff_hypothesis_level_less_than_4 = 15

# the hypothesis refers to the percentage of level-1 college graduates in Amtek's sales staff, which is also mentioned in the premise
if sales_staff_premise_level_1!= sales_staff_hypothesis_level_less_than_4:
    # check if the percentage of level-1 college graduates in the premise contradicts the percentage in the hypothesis
    label = "contradiction"
else:
    # if the percentage in the premise matches the percentage in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
