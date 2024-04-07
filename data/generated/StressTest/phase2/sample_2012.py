# Premise: Jake, Paul and Hari together dig the well in 8 days.
# Hypothesis: Jake, Paul and Hari together dig the well in more than 8 days.
# Golden Label: contradiction

digging_days_premise = 8
digging_days_hypothesis = 8

# the hypothesis refers to the number of digging days mentioned in the premise
if digging_days_hypothesis != digging_days_premise:
    # check if the number of digging days in the hypothesis contradicts the number of digging days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

