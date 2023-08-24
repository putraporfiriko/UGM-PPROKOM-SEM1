howmanysec = int(input("berapa waktu yang anda miliki? "))
secinaday = 60 * 60 * 24

days = howmanysec // secinaday                                  # hari
hours = (howmanysec // (60 * 60)) - (days * 24)                 # jam
minutes = (howmanysec // 60) - (hours * 60) - (days * 60*24)    # menit
detik = howmanysec % 60                                         # detik, mod howmanysec

print(f"waktu anda yang tersisa adalah: {days} Hari, {hours} jam, {minutes} menit, {detik} detik.")

