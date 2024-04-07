# Premise: Ayesha's father was 34 years of age when she was born while her mother was 30 years old when her brother four years younger to her was born.
# Hypothesis: Ayesha's father was more than 24 years of age when she was born while her mother was 30 years old when her brother four years younger to her was born.
# Golden Label: entailment

father_age_premise = 34
father_age_hypothesis = 24
mother_age_premise = 30
mother_age_hypothesis = 30

# the hypothesis talks about the ages of Ayesha's parents when she and her brother were born, which is also mentioned in the premise
if father_age_premise <= father_age_hypothesis:
    # check if the estimate of 'father_age_hypothesis' contradicts the father's age in the premise
    label = "contradiction"
elif mother_age_hypothesis != mother_age_premise:
    # check if the mother's age in the hypothesis contradicts the mother's age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

