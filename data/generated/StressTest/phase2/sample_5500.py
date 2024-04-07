# Premise: If there are less than 720 baseball fans in the town, each of whom is a fan of exactly one of those three teams, how many NY Mets fans are there in this town?
# Hypothesis: If there are 320 baseball fans in the town, each of whom is a fan of exactly one of those three teams, how many NY Mets fans are there in this town?
# Golden Label: neutral

baseball_fans_premise = 720
baseball_fans_hypothesis = 320

# the hypothesis refers to the number of baseball fans in the town mentioned in the premise
if baseball_fans_hypothesis >= baseball_fans_premise:
    # check if the number of baseball fans in the hypothesis contradicts the premise's upper limit
    label = "contradiction"
else:
    # if the number of fans in the hypothesis is less than the upper limit in the premise, it cannot be explicitly entailed from the premise but it doesn't contradict it either
    label = "neutral"

print(label)

