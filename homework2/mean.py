import csv


def avg_height_weight() -> str:
    pounds_to_kg = 0.453592
    inches_to_cm = 2.54
    total_people = 0
    height_sum = 0
    weight_sum = 0

    with open('hw.csv') as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            total_people += 1
            height_sum += float(row[1])
            weight_sum += float(row[2])

        height_avg = round((height_sum / total_people) * inches_to_cm, 2)
        weight_avg = round((weight_sum / total_people) * pounds_to_kg, 2)
        result = f'{height_avg}, {weight_avg}'

        return str(result)
