work_days_renu_premise = 8
work_days_renu_suma_premise = 4
work_days_renu_hypothesis = 4
work_days_renu_suma_hypothesis = 4

# the hypothesis refers to the number of days Renu can do a piece of work alone and with her friend Suma
if work_days_renu_premise != work_days_renu_hypothesis:
    # check if the 'work_days_renu_hypothesis' contradicts the number of work days mentioned in the premise
    label = "contradiction"
elif work_days_renu_suma_premise != work_days_renu_suma_hypothesis:
    # check if 'work_days_renu_suma_hypothesis' contradicts the number of work days with Suma's help mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
