# ages of Amar, Akbar and Anthony in the premise
amar_age_premise = 20
akbar_age_premise = 30
anthony_age_premise = 25

total_ages_premise = amar_age_premise + akbar_age_premise + anthony_age_premise

# ages of Amar, Akbar and Anthony in the hypothesis
amar_age_hypothesis = 25
akbar_age_hypothesis = 35
anthony_age_hypothesis = 30

total_ages_hypothesis = amar_age_hypothesis + akbar_age_hypothesis + anthony_age_hypothesis

# comparing the ages of Amar, Akbar and Anthony in the premise and hypothesis
if total_ages_premise!= total_ages_hypothesis:
    # check if the total ages in the hypothesis contradicts the total ages in the premise
    label = "contradiction"
else:
    # if the total ages in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
