y -1.0 # constant speed of Sacha
y_bruno -5.0 # constant speed of Bruno

sacha_speed_premise = 7.0
sacha_speed_hypothesis = 4.0
bruno_speed_premise = 5.0
bruno_speed_hypothesis = 5.0

# the hypothesis refers to the speed of Sacha and Bruno, which are also mentioned in the premise
if sacha_speed_hypothesis <= sacha_speed_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif bruno_speed_hypothesis!= bruno_speed_premise:
    # check if the speed of Bruno in the hypothesis contradicts the speed of Bruno in the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values do not contradict, we can infer entailment
    label = "entailment"

print(label)
