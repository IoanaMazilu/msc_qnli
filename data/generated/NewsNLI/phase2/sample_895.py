# Premise: In contrast, 28% teens say they never text their friends -- but then, 23% of teens do n't have a cell phone at all.
# Hypothesis: Study finds that 39% of teens say they never exchange e-mail.
# Golden Label: neutral

teens_never_text_premise = 0.28
teens_no_cell_premise = 0.23
teens_never_email_hypothesis = 0.39

# the hypothesis mentions the percentage of teens who never exchange e-mail, which is not referenced in the premise
# the premise talks about the percentages of teens who never text their friends and who do not have a cell phone.
# there is no relation or comparison possible between these two distinct behaviors (texting and emailing), and different groups (those without a cell phone and those who never email)
# so the relation is neutral

label = "neutral"

print(label)

