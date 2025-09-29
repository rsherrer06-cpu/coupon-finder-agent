import streamlit as st
import openai

# Load your OpenAI API key securely from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🤑 Coupon Finder AI Agent")

# Get and clean store name input
store = st.text_input("Enter store name (e.g., nike)").strip().lower()

if st.button("Find Coupons") and store:
    st.write(f"🔍 Searching for coupons for {store}.com...")

    # Simulated coupon list based on store
    store_coupons = {
        "nike": [
            "20% Off Sitewide — Code: NIKE20",
            "Free Shipping Over $50 — Code: SHIPFREE",
            "Buy 1 Get 1 50% Off — Code: BOGO50"
        ],
        "adidas": [
            "25% Off Sneakers — Code: ADI25",
            "Free Returns — Code: RETURNFREE",
            "Extra 10% Off Sale Items — Code: SALE10"
        ],
        "target": [
            "$10 Off $50 — Code: SAVE10",
            "Free Same-Day Delivery — Code: FASTFREE",
            "Buy 2 Get 1 Free — Code: B2G1"
        ]
    }

    # Use store-specific coupons or fallback to generic ones
    coupons = store_coupons.get(store, [
        "10% Off First Order — Code: WELCOME10",
        "Free Shipping — Code: FREESHIP",
        "Seasonal Sale — Code: FALL25"
    ])

    # Show the coupons being analyzed
    st.write("🧾 Coupons being analyzed:")
    st.write(coupons)

    # Create AI prompt
    prompt = (
        f"You are an expert coupon analyst for {store}.com.\n"
        f"Here are the current coupons:\n" + "\n".join(coupons) +
        "\n\nPlease rank them by value and explain which one is best for customers shopping at this store."
    )

    # Call OpenAI to summarize and rank
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    summary = response['choices'][0]['message']['content']
    st.write("✅ AI Summary of Coupons:")
    st.write(summary)
