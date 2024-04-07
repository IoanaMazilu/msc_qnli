# Premise: When Anusha reached the goal post, Banu was less than 30 m behind.
# Hypothesis: When Anusha reached the goal post, Banu was 10 m behind.
# Golden Label: neutral

banu_behind_premise = 30
banu_behind_hypothesis = 10

# the hypothesis talks about the distance Banu was behind Anusha when Anusha reached the goal post, referenced also in the premise
if banu_behind_hypothesis > banu_behind_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance Banu was behind Anusha
    # any distance less than or equal to 'banu_behind_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

