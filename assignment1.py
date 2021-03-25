#Pilot navigation system

altitude=int(input("Please enter the altitude(ft): "))
if(altitude <= 3000):
    print("It is safe to land , you can land")
elif((altitude > 3000)&(altitude <= 6000)):
    print("Try for landing")
else:
    print("Don't land the plane , go around")
