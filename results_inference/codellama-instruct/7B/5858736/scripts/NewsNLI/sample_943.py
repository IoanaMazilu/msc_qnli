costumes_premise = "cover the face"
containers_premise = "more than 1 liter of liquid"
bulky_clothes_premise = "vests with pockets"

deaths_hypothesis = 3
wounded_hypothesis = 260

# the hypothesis mentions the number of deaths and the number of wounded, which are also mentioned in the premise
if deaths_hypothesis!= 3:
    # check if the number of deaths in the hypothesis contradicts the number of deaths reported in the premise
    label = "contradiction"
elif wounded_hypothesis!= 260:
    # check if the number of wounded in the hypothesis contradicts the number of wounded in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
