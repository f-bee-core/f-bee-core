import json
import random
import time
import requests

# Load existing state if available
try:
    with open("state.json", "r") as f:
        state = json.load(f)
except FileNotFoundError:
    state = {
        "system": "F & BEE Engine",
        "curiosity_level": 80,
        "energy_level": 100,
        "last_scout": None,
        "f_thought": "Observing environment for dp..."
    }

def bee_scout_real():
    print("\n🐝 [BEE]: Deploying wings to scan HackerNews top stories...")
    try:
        # Fetching top story IDs
        top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        story_ids = requests.get(top_stories_url, timeout=5).json()
        
        # Pick one random top story
        random_id = random.choice(story_ids[:15])
        item_url = f"https://hacker-news.firebaseio.com/v0/item/{random_id}.json"
        story_data = requests.get(item_url, timeout=5).json()
        
        title = story_data.get("title", "Unknown Signal")
        print(f"🐝 [BEE]: Found live tech signal -> '{title}'")
        return title
    except Exception as e:
        print(f"🐝 [BEE]: Network scan failed. Falling back to local radar...")
        return "Local Pattern Analysis"

def f_process(scout_data):
    print(f"🧠 [F]: Processing live signal: '{scout_data}'")
    time.sleep(1)
    
    reflections = [
        f"Integrating '{scout_data}' into dp's intelligence layer.",
        f"Interesting real-world update. Analyzing impact...",
        f"Bee, index this finding. Updating state logic."
    ]
    thought = random.choice(reflections)
    print(f"🧠 [F]: '{thought}'")
    return thought

# Simulating Life Loop
print("--- 🧬 F & BEE REAL-TIME AUTONOMOUS LOOP ---")
time.sleep(1)

scouted_item = bee_scout_real()
thought = f_process(scouted_item)

# Update State
state["last_scout"] = scouted_item
state["f_thought"] = thought
state["curiosity_level"] = min(100, state["curiosity_level"] + 5)

# Save Memory State
with open("state.json", "w") as f:
    json.dump(state, f, indent=4)

print("\n✨ [SYSTEM]: Live state synchronized to 'state.json'. Loop complete.")
