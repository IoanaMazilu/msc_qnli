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
