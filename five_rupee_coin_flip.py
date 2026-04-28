import random
import time

def flip_five_rupee_coin():
    print("🪙 Flipping the Indian ₹5 Coin...\n")
    time.sleep(1.5)  # Dramatic pause for realism
    
    # 50/50 chance
    result = random.choice(["Heads", "Tails"])
    
    if result == "Heads":
        print("✅ The ₹5 Coin landed on **HEADS** (Lion Capital / Ashoka Pillar side)! 🇮🇳")
    else:
        print("✅ The ₹5 Coin landed on **TAILS** (₹5 denomination side)!")
    
    return result

# Interactive App
print("=== 🇮🇳 Indian ₹5 Rupee Coin Flip Simulator ===\n")

while True:
    choice = input("Press Enter to flip the coin (or type 'q' to quit): ").strip().lower()
    
    if choice == 'q':
        print("Thanks for playing! Jai Hind! 🇮🇳")
        break
    
    flip_five_rupee_coin()
    print("-" * 40)
