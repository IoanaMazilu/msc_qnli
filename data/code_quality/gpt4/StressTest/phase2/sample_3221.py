gokul_madan_diff_premise = 2
madan_age_premise = 5
gokul_madan_diff_hypothesis = 5
madan_age_hypothesis = 5

# the hypothesis talks about the age difference between Gokul and Madan, which is also referenced in the premise
if gokul_madan_diff_premise != gokul_madan_diff_hypothesis:
    # check if the age difference in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
elif madan_age_premise != madan_age_hypothesis:
    # check if the age of Madan in the hypothesis contradicts the age of Madan reported in the premise
    label = "contradiction"
else:
    # the sentences do not provide enough information about Arun's age, so we cannot infer anything about it
    label = "neutral"

print(label)
