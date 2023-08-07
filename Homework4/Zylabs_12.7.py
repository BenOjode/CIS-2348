# ZyLabs 12.7
# Benjamin Ojode
# 1663352

def get_age():
    age = int(input())
    if 18 <= age <= 75:
        return age
    raise ValueError("Invalid age.")

def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * 0.7
    return heart_rate

if __name__ == "__main__":
    try:
        age = get_age()
        print("Fat burning heart rate for a", age, "year-old:", fat_burning_heart_rate(age), "bpm")
    except ValueError as i:
        print(i)
        print("Could not calculate heart rate info.\n")
