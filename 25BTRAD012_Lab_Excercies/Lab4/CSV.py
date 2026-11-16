import csv

with open("employee.csv", "r") as f:
    for e in csv.DictReader(f):
        basic = float(e["Basic"])
        hra = basic * 0.20
        da = basic * 0.10
        gross = basic + hra + da
        deduction = gross * 0.10
        net = gross - deduction

        print(e["Name"], "Gross:", gross,
              "Deduction:", deduction, "Net Salary:", net)