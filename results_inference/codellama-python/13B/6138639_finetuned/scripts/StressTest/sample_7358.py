total_age_premise = 45
total_age_hypothesis = 75

# the hypothesis talks about the total age of Amar, Akbar and Anthony, which is also mentioned in the premise
if total_age_hypothesis!= total_age_premise:
    # check if the total age in the hypothesis contradicts the total age reported in the premise
    label = "contradiction"
else:
    # if the total age in the hypothesis does not contradict the total age in the premise, we can infer entailment
    label = "entailment"

print(label)
