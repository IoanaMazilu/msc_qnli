# Premise: If there are 360 baseball fans in the town, each of whom is a fan of exactly one of those three teams, how many NY Mets fans are there in this town?
# Hypothesis: If there are 760 baseball fans in the town, each of whom is a fan of exactly one of those three teams, how many NY Mets fans are there in this town?
# Golden Label: contradiction

baseball_fans_premise = 360
baseball_fans_hypothesis = 760

# the hypothesis refers to the number of baseball fans in a town mentioned in the premise
if baseball_fans_premise != baseball_fans_hypothesis:
    # check if the number of baseball fans in the hypothesis contradicts the number of baseball fans reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

