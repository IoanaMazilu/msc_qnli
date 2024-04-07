# Premise: Level-less than 4 college graduates account for 15% of Amtek's sales staff.
# Hypothesis: Level-1 college graduates account for 15% of Amtek's sales staff.
# Golden Label: neutral

# define variables 
level_premise = 4
level_hypothesis = 1
percentage_sales_staff_premise = 15
percentage_sales_staff_hypothesis = 15

# the hypothesis refers to the level of college graduates and their percentage in the sales staff, mentioned in the premise
if level_hypothesis >= level_premise:
    # check if the 'level_hypothesis' contradicts the level in the premise
    label = "contradiction"
elif percentage_sales_staff_hypothesis != percentage_sales_staff_premise:
    # check if the percentage of sales staff in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
print(label)

