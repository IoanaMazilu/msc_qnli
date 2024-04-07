# Premise: Raju has scored less than 650 marks and was declared failed by 22 marks.
# Hypothesis: Raju has scored 250 marks and was declared failed by 22 marks.
# Golden Label: neutral

marks_scored_premise = 650
marks_scored_hypothesis = 250
marks_failed_premise = 22
marks_failed_hypothesis = 22

# Both hypothesis and premise refer to the marks scored by Raju and the marks by which he failed
if marks_scored_hypothesis >= marks_scored_premise:
    # Check if the marks scored in the hypothesis contradict the estimate of less than 'marks_scored_premise'
    label = "contradiction"
elif marks_failed_hypothesis != marks_failed_premise:
    # Check if the marks by which Raju failed in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise values, then it can be concluded as entailment
    label = "entailment"

print(label)

