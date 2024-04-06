# Premise: Authorities in Brazil say that more than 200 people are being held hostage in a prison in the country's remote, Amazonian-jungle state of Rondonia.
# Hypothesis: Authorities in Brazil hold 200 people as hostage.
# Golden Label: neutral

hostages_premise = 200
hostages_hypothesis = 200

# the hypothesis talks about the number of hostages held by authorities which is also mentioned in the premise
if hostages_hypothesis > hostages_premise:
    # check if the number of hostages in the hypothesis contradicts the number of hostages from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

