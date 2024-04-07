# Premise: If there are 360 baseball fans in the town, each of whom is a fan of exactly one of those three teams, how many NY Mets fans are there in this town?
# Hypothesis: If there are less than 560 baseball fans in the town, each of whom is a fan of exactly one of those three teams, how many NY Mets fans are there in this town?
# Golden Label: entailment

baseball_fans_premise = 360
baseball_fans_hypothesis = 560

# the hypothesis refers to the number of baseball fans mentioned in the premise
if baseball_fans_hypothesis <= baseball_fans_premise:
    # check if the number of baseball fans in the hypothesis contradicts the number of baseball fans reported in the premise
    label = "contradiction"
else:
    # the premise gives only an exact number for the baseball fans
    # any number of baseball fans less than 'baseball_fans_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

