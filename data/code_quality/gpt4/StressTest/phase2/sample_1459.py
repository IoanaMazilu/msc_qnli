# define numerical variables
work_hours_mon_wed_fri_premise = 4
work_hours_mon_wed_fri_hypothesis = 8
work_hours_tue_thu_premise = 6
work_hours_tue_thu_hypothesis = 6

# The hypothesis assumes that Sheila works 8 hours per day on Monday, Wednesday, and Friday
if work_hours_mon_wed_fri_hypothesis <= work_hours_mon_wed_fri_premise:
    # Check if the hypothesis contradicts the premise where Sheila works more than 4 hours per day on Monday, Wednesday, and Friday
    label = "contradiction"
elif work_hours_tue_thu_hypothesis != work_hours_tue_thu_premise:
    # Check if the hypothesis contradicts the premise where Sheila works 6 hours per day on Tuesday and Thursday
    label = "contradiction"
else:
    # Since the premise only suggests that Sheila works more than 4 hours on Monday, Wednesday, and Friday, it cannot explicitly entail that she works exactly 8 hours on these days. Therefore, the relation is neutral.
    label = "neutral"

print(label)
