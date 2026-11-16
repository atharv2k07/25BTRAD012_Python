f = "students.txt"
open(f, "a").close()

while True:
    print("\n1.Add 2.Display 3.Search 4.Update 5.Exit")
    c = input("Choice: ")

    if c == "1":
        open(f, "a").write(input("Roll,Name,Marks: ") + "\n")

    elif c == "2":
        print(open(f).read())

    elif c == "3":
        r = input("Roll: ")
        print(next((s for s in open(f) if s.startswith(r+",")), "Not found"))

    elif c == "4":
        r = input("Roll: ")
        lines = [input("New data: ")+"\n" if s.startswith(r+",") else s for s in open(f)]
        open(f, "w").writelines(lines)

    elif c == "5":
        break