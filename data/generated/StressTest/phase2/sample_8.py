# Premise: Renu can do a piece of work in 8 days, but with the help of her friend Suma, she can do it in 4 days.
# Hypothesis: Renu can do a piece of work in 2 days, but with the help of her friend Suma, she can do it in 4 days.
# Golden Label: contradiction

work_days_renu_premise = 8
work_days_renu_suma_premise = 4
work_days_renu_hypothesis = 2
work_days_renu_suma_hypothesis = 4

# the hypothesis refers to the number of days needed for Renu (with and without Suma) to do a piece of work, also mentioned in the premise
if work_days_renu_hypothesis != work_days_renu_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
elif work_days_renu_suma_hypothesis != work_days_renu_suma_premise:
    # check if the number of days with Suma's help in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

