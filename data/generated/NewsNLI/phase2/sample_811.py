# Premise: Seven school employees have been placed on paid emergency leave by the Texas Department of Aging and Disability Services, according to spokeswoman Cecilia Fedorov.
# Hypothesis: Seven school employees placed on leave ; arrest warrants are pending.
# Golden Label: neutral

employees_leave_premise = 7
employees_leave_hypothesis = 7

# the hypothesis mentions the number of school employees placed on leave, which is also referenced in the premise
# however, the hypothesis also mentions pending arrest warrants, which cannot be entailed from the premise
label = "neutral"

print(label)

