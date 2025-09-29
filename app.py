import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🤑 Coupon Finder AI Agent")

store = st.text_input("Enter store name (e.g., nike)")

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

coupons = store_coupons.get(store.lower(), [
    "10% Off First Order — Code: WELCOME10",
    "Free Shipping — Code: FREESHIP",
    "Seasonal Sale — Code: FALL25"
])


    prompt = f"Summarize and rank these coupon codes for {store}.com:\n" + "\n".join(coupons)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    summary = response['choices'][0]['message']['content']
    st.write("✅ AI Summary of Coupons:")
    st.write(summary)
