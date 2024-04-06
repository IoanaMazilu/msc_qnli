# Premise: Employers cut 533K jobs in Nov., most in 34 years.
# Hypothesis: 533,000 jobs lost in November, most in 34 years.
# Golden Label: entailment

jobs_lost_premise = 533000
jobs_lost_hypothesis = 533000
years_premise = 34
years_hypothesis = 34

# the hypothesis and premise mention the number of jobs lost and the period over which it is the most
if jobs_lost_hypothesis != jobs_lost_premise:
    # check if the number of jobs lost in the hypothesis contradicts the number of jobs lost in the premise
    label = "contradiction"
elif years_hypothesis != years_premise:
    # check if the years in the hypothesis contradicts the years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

