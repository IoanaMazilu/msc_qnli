# Premise: Fed raises rates again, sees two more hikes in 2018.
# Hypothesis: Fed hikes rates, signals two more for 2018.
# Golden Label: entailment

hikes_already_done_premise = 1
hikes_already_done_hypothesis = 1
more_hikes_premise = 2
more_hikes_hypothesis = 2

# the hypothesis and premise mention the number of hikes already done by the Fed and the number of more hikes it signals for the rest of the year
if hikes_already_done_premise != hikes_already_done_hypothesis:
    # check if the number of hikes already done in the hypothesis contradicts the number of hikes already done in the premise
    label = "contradiction"
elif more_hikes_premise != more_hikes_hypothesis:
    # check if the number of more hikes in the hypothesis contradicts the number of more hikes in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

