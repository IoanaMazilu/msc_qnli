# Premise: The monthly income of Suman in the year 2009 was approximately what percentage of the monthly income of Jyothi in the year 2010?
# Hypothesis: The monthly income of Suman in the year more than 1009 was approximately what percentage of the monthly income of Jyothi in the year 2010?
# Golden Label: entailment

# There are no specific numerical entities or quantities specified in the premise and hypothesis
# However, there is a inconsistency in the years mentioned for Suman's income in the premise and hypothesis

year_suman_premise = 2009
year_suman_hypothesis = 1009

# the hypothesis refers to the year of Suman's income mentioned in the premise
if year_suman_hypothesis != year_suman_premise:
    # check if the year of Suman's income in the hypothesis contradicts the year mentioned in the premise
    label = "contradiction"
else:
    # if the years match, then neither entailment nor contradiction can be inferred as the premise and hypothesis are asking a question without providing specific quantities
    label = "neutral"

print(label)

