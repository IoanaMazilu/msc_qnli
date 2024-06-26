sales_staff_premise = 15
sales_staff_hypothesis = 15

# the hypothesis is referring to the percentage of college graduates in the sales staff mentioned in the premise
if sales_staff_hypothesis != sales_staff_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # the premise gives no indication about the level of the college graduates
    # so the level of the graduates cannot be compared or inferred from the premise
    label = "neutral"

print(label)
