import calendar
import itertools

blank = "&nbsp;"

myCal = calendar.monthcalendar(2011,9)
day_names = itertools.cycle(['mon','tue','wed','thu','fri','sat','sun']) # endless list
cal = [day for week in myCal for day in week] # flatten list of lists

# empty lists to hold the data
headers = []
numbers = []
imgs = []

# fill lists
for d in cal:
    if d != 0:
        headers.append(day_names.next())
        numbers.append(d)
        imgs.append("image"+str(d))
    else:
        headers.append(day_names.next())
        numbers.append(blank)
        imgs.append(blank)

# format data
html = "<table><tr></tr>{0}<tr>{1}</tr><tr>{2}</tr></table>".format(
    "".join(["<td>%s</td>"% h for h in headers]),
    "".join(["<td>%s</td>"% n for n in numbers]),
    "".join(["<td>%s</td>"% i for i in imgs]))
