# Premise: If there are more than 130 baseball fans in the town, each of whom is a fan of exactly one of those three teams, how many NY Mets fans are there in this town?
# Hypothesis: If there are 330 baseball fans in the town, each of whom is a fan of exactly one of those three teams, how many NY Mets fans are there in this town?
# Golden Label: neutral

baseball_fans_premise = 130
baseball_fans_hypothesis = 330

# the hypothesis refers to the number of baseball fans in the town mentioned in the premise
if baseball_fans_hypothesis <= baseball_fans_premise:
    # check if the number of baseball fans in the hypothesis contradicts the estimate of more than 'baseball_fans_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of baseball fans
    # any number of fans greater than 'baseball_fans_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

