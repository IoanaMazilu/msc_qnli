percentage_saved_premise = 10
percentage_saved_hypothesis = 40

# the hypothesis refers to the saving percentage of Kishore's salary mentioned in the premise
if percentage_saved_hypothesis == percentage_saved_premise:
    # check if the saving percentage in the hypothesis matches the saving percentage in the premise
    label = "entailment"
elif percentage_saved_hypothesis < percentage_saved_premise:
    # check if the saving percentage in the hypothesis contradicts the saving percentage reported in the premise
    label = "contradiction"
else:
    # the hypothesis value is larger than the premise one, so it could be possible but it cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
