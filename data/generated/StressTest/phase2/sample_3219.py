# Premise: If Gokul is 2 years younger to Madan whose age is 5 years, then what is the age of Arun?
# Hypothesis: If Gokul is less than 8 years younger to Madan whose age is 5 years, then what is the age of Arun?
# Golden Label: entailment

gokul_age_diff_premise = 2
gokul_age_diff_hypothesis = 8
madan_age_premise = 5
madan_age_hypothesis = 5

# the hypothesis refers to the age difference between Gokul and Madan mentioned in the premise
if gokul_age_diff_hypothesis < gokul_age_diff_premise:
    # check if the hypothesis age difference contradicts the age difference in the premise
    label = "contradiction"
elif madan_age_hypothesis != madan_age_premise:
    # check if the age of Madan in the hypothesis contradicts the age of Madan reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

