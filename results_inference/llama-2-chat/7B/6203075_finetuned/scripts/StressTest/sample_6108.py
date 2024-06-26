level_premise = 1
level_hypothesis = 4
sales_staff_premise = 0.15
sales_staff_hypothesis = 0.15

# the hypothesis refers to the percentage of sales staff that are level-1 college graduates, as mentioned in the premise
if level_hypothesis <= level_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives a specific percentage for level-1 college graduates
    # any percentage greater than 'level_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
