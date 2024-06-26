people_premise = 6
people_hypothesis = 4

# the hypothesis refers to the number of people from which a committee is to be selected, also mentioned in the premise
if people_premise <= people_hypothesis:
    # check if the number of 'people_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
elif people_premise > people_hypothesis:
    # check if the number of people in the hypothesis can be explicitly entailed from the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we infer neutrality
    label = "neutral"

print(label)
