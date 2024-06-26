renu_work_days_premise = 6
suma_help_days_premise = 5
renu_work_days_hypothesis = 2
suma_help_days_hypothesis = 5

# the hypothesis refers to how many days Renu can do a piece of work alone and with Suma's help
if renu_work_days_hypothesis != renu_work_days_premise:
    # check if the number of days Renu can do the work alone in the hypothesis contradicts the number from the premise
    label = "contradiction"
elif suma_help_days_hypothesis != suma_help_days_premise:
    # check if the number of days Renu can do the work with Suma's help in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
