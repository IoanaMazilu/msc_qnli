# Premise: Deficit Will Hit $1.845 Trillion This Year, Congressional Budget Office (CBO) Says.
# Hypothesis: US deficit forecast to hit $1.8 trillion this year.
# Golden Label: entailment

deficit_premise = 1.845
deficit_hypothesis = 1.8

# the hypothesis and premise mention the amount of US deficit for this year
if deficit_hypothesis > deficit_premise:
    # check if the deficit value in the hypothesis contradicts the deficit value in the premise
    label = "contradiction"
elif deficit_hypothesis < deficit_premise:
    # the premise gives only an estimate for the deficit
    # any estimate of the deficit in the hypothesis less than 'deficit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

