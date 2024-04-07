# Premise: Renu can do a piece of work in 6 days, but with the help of her friend Suma, she can do it in 3 days.
# Hypothesis: Renu can do a piece of work in 8 days, but with the help of her friend Suma, she can do it in 3 days.
# Golden Label: contradiction

renu_work_days_premise = 6
renu_suma_work_days_premise = 3
renu_work_days_hypothesis = 8
renu_suma_work_days_hypothesis = 3

# the hypothesis refers to the number of days Renu can do a piece of work alone and with the help of Suma
if renu_work_days_hypothesis != renu_work_days_premise:
    # check if the number of days Renu can do the work alone in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
elif renu_suma_work_days_hypothesis != renu_suma_work_days_premise:
    # check if the number of days Renu and Suma can do the work together in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

