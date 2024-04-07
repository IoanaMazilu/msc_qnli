# Premise: Renu can do a piece of work in 5 days, but with the help of her friend Suma, she can do it in 4 days.
# Hypothesis: Renu can do a piece of work in more than 5 days, but with the help of her friend Suma, she can do it in 4 days.
# Golden Label: contradiction

work_days_renu_premise = 5
work_days_renu_hypothesis = 5
work_days_renu_suma_premise = 4
work_days_renu_suma_hypothesis = 4

# the hypothesis refers to the time Renu and Renu with Suma take to finish a task, mentioned in the premise
if work_days_renu_premise < work_days_renu_hypothesis:
    # check if the 'work_days_renu_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
elif work_days_renu_suma_hypothesis != work_days_renu_suma_premise:
    # check if the number of work days in the hypothesis contradicts the number of work days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

