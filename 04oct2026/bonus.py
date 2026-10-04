working_year=int(input("enter the working years:"))
performance_rating=int(input("enter the rating:"))
if performance_rating>4 or working_year>2:
    print("eligible")
else:
    print("not eligible")