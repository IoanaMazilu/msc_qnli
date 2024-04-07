# Premise: Ayisha's father's age will be twice Shankar's age after 10 years.
# Hypothesis: Ayisha's father's age will be twice Shankar's age after 30 years.
# Golden Label: contradiction

years_premise = 10
years_hypothesis = 30

# the hypothesis talks about the doubling of Shankar's age in relation to Ayisha's father's age, similarly mentioned in the premise
if years_hypothesis != years_premise:
    # check if the hypothesis years contradicts the years mentioned in the premise
    label = "contradiction"
else:
    # if the years in the hypothesis do not contradict the years in the premise, we can infer entailment
    label = "entailment"

print(label)

