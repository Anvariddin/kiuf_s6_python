def convert_mm_to_m_cm_mm(mm):
    meters = mm // 1000
    remaining_mm = mm % 1000
    centimeters = remaining_mm // 10
    remaining_mm %= 10
    millimeters = remaining_mm

    return meters, centimeters, millimeters

mm = int(input("Uzunlikni kiriting: "))
convert_mm_to_m_cm_mm(mm)

meters, centimeters, millimeters = convert_mm_to_m_cm_mm(mm)
print(f"{mm} mm teng {meters} meterga, {centimeters} centimeterga, and {millimeters} millimeterga.")
