import sys

input_data = sys.argv[-1]
f = open(input_data, 'r')
lines = f.read().strip().split('\n')

total_safe = 0 #variable for how many safe reports we have in total
unsafe = []#to be used for part 2
for line in lines:
    report = line.split()
    #all_increasing = False
    #for each report check if all levels are strictly increasing or decreasing by 1 <= diff <= 3
    prev = int(report[0])
    increasing = False
    decreasing = False
    safe = True
    for i in range(1, len(report)):#for every level in report
        curr = int(report[i])
        diff = curr - prev#the difference between current and previous level
        if diff<0:
            decreasing = True
        elif diff>0:
            increasing = True
        if increasing and decreasing:#if we've found both increasing and decreasing trends mark unsafe
            safe = False
            unsafe.append(report)
            break
        if 1 <= abs(diff) <= 3:
            pass
        else:#if difference is outside of bounds for any 2 consecutive levels mark unsafe
            safe = False
            unsafe.append(report)
            break
        prev = curr

    if safe:
        total_safe += 1

print(total_safe)

#part 2
#we follow same steps but this time, if removing one level from a
#report would make it safe, we count it as safe
second_total_safe = 0
for report in unsafe:
    reports = []
    for u in range(len(report)):
        curr_report = report.copy()
        curr_report.pop(u)
        reports.append(curr_report)
    for report in reports:
        all_increasing = False
        #for each report check if all levels are strictly increasing or decreasing by 1 <= diff <= 3
        prev = int(report[0])
        increasing = False
        decreasing = False
        safe = True
        for i in range(1, len(report)):#for every level in report
            curr = int(report[i])
            diff = curr - prev#the difference between current and previous level
            if diff<0:
                decreasing = True
            elif diff>0:
                increasing = True
            if increasing and decreasing:#if we've found both increasing and decreasing trends mark unsafe
                safe = False
                break
            if 1 <= abs(diff) <= 3:
                pass
            else:#if difference is outside of bounds for any 2 consecutive levels mark unsafe
                safe = False
                break
            prev = curr

        if safe:
            second_total_safe += 1
            break

print(total_safe+second_total_safe)