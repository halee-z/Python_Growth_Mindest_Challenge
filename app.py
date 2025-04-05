import streamlit as st
import random
import datetime
import os

# List of growth mindset challenges
challenges = [
    "Write down 3 things you learned from a recent mistake.",
    "Try something new that scares you a little.",
    "Give yourself a compliment and mean it!",
    "Help someone else without expecting anything in return.",
    "Reflect on a failure and what it taught you.",
    "Learn a new word and use it in a sentence.",
    "Write about a time when you didn’t give up.",
    "Spend 10 minutes journaling your thoughts.",
    "Think of a role model and list why they inspire you.",
    "Read or watch something educational today."
]

# File to save progress (for local use)
progress_file = "growth_mindset_progress.txt"

# Load progress
def load_progress():
    if os.path.exists(progress_file):
        with open(progress_file, "r") as file:
            return int(file.read())
    return 0

# Save progress
def save_progress(count):
    with open(progress_file, "w") as file:
        file.write(str(count))

# Streamlit UI
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱")
st.title("🌱 Growth Mindset Daily Challenge")
st.write(f"📅 Today's Date: {datetime.date.today().strftime('%B %d, %Y')}")

# Display today's challenge
challenge = random.choice(challenges)
st.subheader("🧠 Today's Challenge")
st.info(challenge)

# Completion button
if st.button("✅ I did it!"):
    count = load_progress() + 1
    save_progress(count)
    st.success(f"Awesome! You've completed {count} challenge(s)! 🌟")
elif st.button("❌ Not yet"):
    st.warning("No worries! Come back when you're ready. 💪")

# Show total completed
st.markdown("---")
st.write(f"🌟 Total Challenges Completed: **{load_progress()}**")
