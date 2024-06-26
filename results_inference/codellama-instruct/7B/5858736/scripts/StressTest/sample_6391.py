sacha_speed_premise = 1
sacha_speed_hypothesis = 6
bruno_speed_premise = 5
bruno_speed_hypothesis = 5

# the hypothesis talks about the speed of Sacha and Bruno, referenced also in the premise
if sacha_speed_hypothesis <= sacha_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than'sacha_speed_premise'
    label = "contradiction"
elif bruno_speed_hypothesis!= bruno_speed_premise:
    # check if the hypothesis value contradicts the estimate of 'bruno_speed_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
