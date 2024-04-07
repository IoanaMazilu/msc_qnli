# Premise: If there are 352 baseball fans in the town, each of whom is a fan of exactly one of those three teams, how many NY Mets fans are there in this town?
# Hypothesis: If there are more than 352 baseball fans in the town, each of whom is a fan of exactly one of those three teams, how many NY Mets fans are there in this town?
# Golden Label: contradiction

baseball_fans_premise = 352
baseball_fans_hypothesis = 352

# the hypothesis talks about the number of baseball fans in a town, referenced also in the premise
if baseball_fans_hypothesis > baseball_fans_premise:
    # check if the hypothesis value contradicts with the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

