# make a program that converts seconds to days, hours, minutes, and seconds
# input: seconds   
# output: days, hours, minutes, and seconds

# input
seconds = int(input("Enter seconds: "))
# process
days = seconds // (24 * 3600)
seconds = seconds % (24 * 3600)
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
# output
print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

