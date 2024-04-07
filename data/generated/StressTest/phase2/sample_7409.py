# Premise: Sam wrote 7 letters on Tuesday and 3 letters on Wednesday.
# Hypothesis: Sam wrote 3 letters on Tuesday and 3 letters on Wednesday.
# Golden Label: contradiction

letters_tuesday_premise = 7
letters_wednesday_premise = 3
letters_tuesday_hypothesis = 3
letters_wednesday_hypothesis = 3

# the hypothesis refers to the number of letters written by Sam on Tuesday and Wednesday, as mentioned in the premise
if letters_tuesday_hypothesis != letters_tuesday_premise:
    # check if the number of letters written on Tuesday in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif letters_wednesday_hypothesis != letters_wednesday_premise:
    # check if the number of letters written on Wednesday in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

