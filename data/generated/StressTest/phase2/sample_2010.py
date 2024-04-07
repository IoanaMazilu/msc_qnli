# Premise: Jake, Paul and Hari together dig the well in 8 days.
# Hypothesis: Jake, Paul and Hari together dig the well in more than 7 days.
# Golden Label: entailment

digging_days_premise = 8
digging_days_hypothesis = 7

# the hypothesis refers to the number of days Jake, Paul and Hari take to dig the well mentioned in the premise
if digging_days_hypothesis >= digging_days_premise:
    # check if the estimate of 'digging_days_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
elif digging_days_hypothesis < digging_days_premise:
    # check if the estimate of 'digging_days_hypothesis' contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"
    
print(label)

