# define variables for numerical entities in the premise and hypothesis
graduate_premise = 4
sales_staff_premise = 15
level_hypothesis = 1

# define variables for numerical entities in the hypothesis
sales_staff_hypothesis = 15

# compare the variables to determine the label
if sales_staff_hypothesis <= sales_staff_premise:
    # check if the hypothesis value contradicts the estimate of'sales_staff_premise'
    label = "contradiction"
elif level_hypothesis!= graduate_premise:
    # check if the number of level 1 college graduates in the hypothesis contradicts the number of level-less than 4 college graduates reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
