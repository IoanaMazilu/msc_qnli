lilly_fishes_premise = 40
rosy_fishes_premise = 7
lilly_fishes_hypothesis = 10
rosy_fishes_hypothesis = 7

# The hypothesis refers to the number of fishes Lilly and Rosy have, which is mentioned also in the premise
if lilly_fishes_hypothesis >= lilly_fishes_premise:
    # Check if the number of Lilly's fishes in the hypothesis contradicts the estimate of less than 'lilly_fishes_premise'
    label = "contradiction"
elif rosy_fishes_hypothesis != rosy_fishes_premise:
    # Check if the number of Rosy's fishes in the hypothesis contradicts the number of Rosy's fishes reported in the premise
    label = "contradiction"
elif lilly_fishes_hypothesis < lilly_fishes_premise and rosy_fishes_hypothesis == rosy_fishes_premise:
    # The premise gives only an estimate for the number of Lilly's fishes
    # Any number of Lilly's fishes less than 'lilly_fishes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    label = "neutral"

print(label)
