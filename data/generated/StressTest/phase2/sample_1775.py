# Premise: The monthly income of Suman in the year 2009 was approximately what percentage of the monthly income of Jyothi in the year 2010?
# Hypothesis: The monthly income of Suman in the year 5009 was approximately what percentage of the monthly income of Jyothi in the year 2010?
# Golden Label: contradiction

year_premise = 2009
year_hypothesis = 5009

# the hypothesis talks about the same comparison as the premise but in a different year
if year_premise != year_hypothesis:
    # the year in the hypothesis is different from the year in the premise
    label = "contradiction"
else:
    # if the year in the hypothesis is the same as in the premise, we could infer entailment
    label = "entailment"

print(label)

