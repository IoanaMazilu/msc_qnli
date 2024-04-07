# Premise: Jake, Paul and Hari together dig the well in 8 days.
# Hypothesis: Jake, Paul and Hari together dig the well in more than 3 days.
# Golden Label: entailment

digging_days_premise = 8
digging_days_hypothesis = 3

# the hypothesis refers to the number of days Jake, Paul and Hari take to dig a well, which is also mentioned in the premise
if digging_days_premise < digging_days_hypothesis:
    # check if the number of days in the premise contradicts the estimate of more than 'digging_days_hypothesis'
    label = "contradiction"
elif digging_days_premise == digging_days_hypothesis:
    # check if the number of days in the premise contradicts the estimate of more than 'digging_days_hypothesis'
    label = "contradiction"
else:
    # if the number of days in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)

