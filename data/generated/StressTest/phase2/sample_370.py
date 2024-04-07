# Premise: If there are less than 560 baseball fans in the town, each of whom is a fan of exactly one of those three teams, how many NY Mets fans are there in this town?
# Hypothesis: If there are 360 baseball fans in the town, each of whom is a fan of exactly one of those three teams, how many NY Mets fans are there in this town?
# Golden Label: neutral

baseball_fans_premise = 560
baseball_fans_hypothesis = 360

# the hypothesis refers to the same town's baseball fans mentioned in the premise
if baseball_fans_hypothesis >= baseball_fans_premise:
    # check if the number of baseball fans in the hypothesis contradicts the estimate of less than 'baseball_fans_premise'
    label = "contradiction"
else:
    # if the number of baseball fans in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

