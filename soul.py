import json
import random
import time

# Default State (Orrma & Mood)
state = {
    "system": "F & BEE Engine",
    "curiosity_level": 80,
    "energy_level": 100,
    "last_scout": None,
    "f_thought": "Observing environment for dp..."
}

def bee_scout():
    topics = ["Quantum Computing", "Rust Async Engine", "Ethical Hacking", "AI Memory Architecture"]
    found = random.choice(topics)
    print(f"\n🐝 [BEE]: Master! I scanned the web and retrieved data on: '{found}'")
    return found

def f_process(scout_data):
    print(f"🧠 [F]: Analyzing input regarding '{scout_data}'...")
    time.sleep(1)
    
    reflections = [
        f"This pattern in {scout_data} can optimize our core flow.",
        f"Fascinating structure. Updating state.json for dp's review.",
        f"Bee, good job. Store this in persistent context."
    ]
    thought = random.choice(reflections)
    print(f"🧠 [F]: '{thought}'")
    return thought

# Simulating Life Loop
print("--- 🧬 F & BEE AUTONOMOUS LOOP STARTED ---")
time.sleep(1)

scouted_item = bee_scout()
thought = f_process(scouted_item)

# Update State
state["last_scout"] = scouted_item
state["f_thought"] = thought
state["curiosity_level"] = min(100, state["curiosity_level"] + 5)

# Save Memory State
with open("state.json", "w") as f:
    json.dump(state, f, indent=4)

print("\n✨ [SYSTEM]: Memory saved to 'state.json'. Living loop complete.")
