# Premise: In one case five workers at a plating company were asphyxiated by hydrogen cyanide while trying to clean a sludge tank.
# Hypothesis: Cyanide fumes killed five workers cleaning one tank.
# Golden Label: entailment

workers_premise = 5
workers_hypothesis = 5
tanks_premise = 1
tanks_hypothesis = 1

# the hypothesis talks about the number of workers killed and the number of tanks involved, which are also mentioned in the premise
if workers_hypothesis != workers_premise:
    # check if the number of workers in the hypothesis contradicts the number of workers from the premise
    label = "contradiction"
elif tanks_hypothesis != tanks_premise:
    # check if the number of tanks in the hypothesis contradicts the number of tanks in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

