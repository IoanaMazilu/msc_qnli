lunch_hamburgers_premise = 9.0
lunch_hamburgers_hypothesis = 6.0

# compare the number of hamburgers served and left over
if lunch_hamburgers_premise - lunch_hamburgers_hypothesis!= 0:
    # if the number of hamburgers served and left over in the hypothesis contradicts the premise, label it as contradiction
    label = "contradiction"
elif lunch_hamburgers_hypothesis == 0:
    # if the hypothesis value is 0, it implies that all hamburgers were served, which contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
