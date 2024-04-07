# Premise: If less than 7 years are subtracted from the present age of Arun and the remainder is divided by 18, then the present age of his grandson Gokul is obtained.
# Hypothesis: If 6 years are subtracted from the present age of Arun and the remainder is divided by 18, then the present age of his grandson Gokul is obtained.
# Golden Label: neutral

years_subtracted_premise = 7
years_subtracted_hypothesis = 6

# the hypothesis talks about the same process of calculating Gokul's age as the premise, but with a different number of years subtracted from Arun's age
if years_subtracted_hypothesis >= years_subtracted_premise:
    # check if the hypothesis value contradicts the estimate of less than 'years_subtracted_premise'
    label = "contradiction"
elif years_subtracted_hypothesis != years_subtracted_premise - 1:
    # check if the number of years subtracted in the hypothesis is not exactly one less than in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise and is exactly one less than in the premise, we can infer entailment
    label = "entailment"

print(label)

