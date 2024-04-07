# Premise: She turns around to head home after a short water break, how fast does Sasha need to ride, in miles per hour, to get home at more than 1 PM?
# Hypothesis: She turns around to head home after a short water break, how fast does Sasha need to ride, in miles per hour, to get home at 5 PM?
# Golden Label: neutral

home_time_premise = 1
home_time_hypothesis = 5

# both the premise and the hypothesis talk about the time Sasha needs to get home
if home_time_hypothesis < home_time_premise:
    # check if the hypothesis time contradicts the premise time estimate
    label = "contradiction"
elif home_time_hypothesis > home_time_premise:
    # the premise gives only an estimate time for Sasha to get home
    # any time after the 'home_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis time and premise time are the same, we can infer entailment
    label = "entailment"

print(label)

