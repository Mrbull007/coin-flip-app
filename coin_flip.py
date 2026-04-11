import random
import time

def coin_flip():
    print("🪙 Welcome to Coin Flip App! 🪙\n")
    
    while True:
        input("Press Enter to flip the coin... (or type 'q' to quit)\n")
        
        print("Flipping the coin...")
        time.sleep(1.5)  # Dramatic effect
        
        result = random.choice(["Heads", "Tails"])
        
        if result == "Heads":
            print("🎉 Result: **HEADS** 🎉\n")
        else:
            print("🎉 Result: **TAILS** 🎉\n")
        
        again = input("Flip again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    coin_flip()
