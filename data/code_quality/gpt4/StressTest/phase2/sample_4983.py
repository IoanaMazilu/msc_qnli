father_age_premise = 58
father_age_hypothesis = 48
mother_age_premise = 42
mother_age_hypothesis = 42

# the hypothesis refers to the age of Ayesha's parents when she and her brother were born, as stated in the premise
if father_age_premise <= father_age_hypothesis:
    # check if the 'father_age_hypothesis' contradicts the age of the father when Ayesha was born as stated in the premise
    label = "contradiction"
elif mother_age_hypothesis != mother_age_premise:
    # check if the age of the mother when Ayesha's brother was born in the hypothesis contradicts the age of the mother when Ayesha's brother was born as reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
