# Premise: Dow Hits 20000 for First Time.
# Hypothesis: Boom: Dow hits 20,000 for first time ever.
# Golden Label: entailment

premise_dow = 20000
hypothesis_dow = 20000

# the hypothesis and premise mention the Dow reaching a certain level for the first time
if premise_dow != hypothesis_dow:
    # check if the level of the Dow in the hypothesis contradicts the level of the Dow in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

