sacha_speed_premise = 6
sacha_speed_hypothesis = 3
bruno_speed_premise = 5
bruno_speed_hypothesis = 5

# the hypothesis refers to the speeds of Sacha and Bruno mentioned in the premise
if sacha_speed_hypothesis!= sacha_speed_premise:
    # check if the hypothesis value contradicts the speed of Sacha in the premise
    label = "contradiction"
elif bruno_speed_hypothesis!= bruno_speed_premise:
    # check if the hypothesis value contradicts the speed of Bruno in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
