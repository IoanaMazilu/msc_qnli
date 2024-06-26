watermelons_premise = 200
watermelons_hypothesis = 100

# the hypothesis talks about the number of watermelons Mike had, referenced also in the premise
if watermelons_hypothesis!= watermelons_premise:
    # check if the number of watermelons in the hypothesis contradicts the number of watermelons reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
