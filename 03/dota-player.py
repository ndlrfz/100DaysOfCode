# Do you want to become Dota2 Player?
# Yes -> Lanjut
# No -> exit
#
# If Yes:
#     What role you want? Mid Off Carry Support
# If Mid:
#     Do this and that
#     exit
print("""
8888888b.   .d88888b. 88888888888     d8888  .d8888b. 
888  "Y88b d88P" "Y88b    888        d88888 d88P  Y88b
888    888 888     888    888       d88P888        888
888    888 888     888    888      d88P 888      .d88P
888    888 888     888    888     d88P  888  .od888P" 
888    888 888     888    888    d88P   888 d88P"     
888  .d88P Y88b. .d88P    888   d8888888888 888"      
8888888P"   "Y88888P"     888  d88P     888 888888888 
""")

ask_play = input("Do you want to play Dota2? Y/N\n")

if ask_play == "Y":
    ask_role = input("What the role you want to play? mid/carry/support/offlane\n")

    if ask_role == "mid":
        print(f"You choose {ask_role} role, make sure you can out lasthit and out-harras enemy midlaner.")
    elif ask_role == "carry":
        print(f"You choose {ask_role} role, make sure you understand how to CS and play the map.")
    elif ask_role == "support":
        print(f"You're good boy as a {ask_role}, be patient about stupidity of your carry.")
    elif ask_role == "offlane":
        print(f"As an {ask_play}, do not triggered when you died so many times in lanes.")
    else:
        print("Enter the correct role.")
else:
    print("OK, I'm out!")
