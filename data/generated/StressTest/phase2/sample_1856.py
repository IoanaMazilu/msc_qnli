# Premise: 4200 among John, Jose & Binoy in the ration 2:4:6.
# Hypothesis: less than 4200 among John, Jose & Binoy in the ration 2:4:6.
# Golden Label: contradiction

total_premise = 4200
total_hypothesis = 4200

# the hypothesis talks about the total amount among John, Jose & Binoy
if total_hypothesis >= total_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)

