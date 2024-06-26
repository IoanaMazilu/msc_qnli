josh_pencils_premise = 142.0
josh_pencils_given_premise = 31.0
josh_pencils_left_hypothesis = 106.0

# the hypothesis refers to the number of pencils left with Josh, which can be calculated from the premise
# compute the number of pencils left with Josh in the premise
josh_pencils_left_premise = josh_pencils_premise - josh_pencils_given_premise
if josh_pencils_left_hypothesis!= josh_pencils_left_premise:
    # check if the number of pencils left in the hypothesis contradicts the number of pencils left in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
