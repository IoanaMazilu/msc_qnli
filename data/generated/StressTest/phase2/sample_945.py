# Premise: Victor has 15 cups if flour, 16 cups of sugar and 8 cups of milk.
# Hypothesis: Victor has less than 35 cups if flour, 16 cups of sugar and 8 cups of milk.
# Golden Label: entailment

flour_cups_premise = 15
flour_cups_hypothesis = 35
sugar_cups_premise = 16
sugar_cups_hypothesis = 16
milk_cups_premise = 8
milk_cups_hypothesis = 8

# the hypothesis talks about the number of cups for each ingredient Victor has, referenced also in the premise
if flour_cups_premise >= flour_cups_hypothesis:
    # check if the hypothesis value contradicts the number of flour cups in the premise
    label = "contradiction"
elif sugar_cups_premise != sugar_cups_hypothesis or milk_cups_premise != milk_cups_hypothesis:
    # check if the number of sugar or milk cups in the hypothesis contradicts the number of sugar or milk cups in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

