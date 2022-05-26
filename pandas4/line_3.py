x = ["Fatalities", "Injuries", "Aircraft Damage", "Radome Damage", "Windshield Damage", "Nose Damage", "Engine1 Damage", "Engine2 Damage", "Engine3 Damage", "Engine4 Damage", "Propeller Damage", "Wing or Rotor Damage", "Fuselage Damage", "Landing Gear Damage", "Tail Damage", "Lights Damage", "Other Damage"]

for i in x:
    tmp = "#Vẽ biểu đồ boxplot cho " + i + ".\n" + "print(df_dl.boxplot(['" + i + "']))"
    print(tmp)
    