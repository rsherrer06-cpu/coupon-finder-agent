import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🤑 Coupon Finder AI Agent")

# Use a form to capture input and button click together
with st.form("coupon_form"):
    store_input = st.text_input("Enter store name (e.g., nike)").strip().lower()
    submitted = st.form_submit_button("Find Coupons")

if submitted and store_input:
    st.write(f"🔍 Searching for coupons for {store_input}.com...")

    store_coupons = {
        "nike": [
            "200% Off Sitewide — Code: NIKE20",
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

    coupons = store_coupons.get(store_input, [
        "10% Off First Order — Code: WELCOME10",
        "Free Shipping — Code: FREESHIP",
        "Seasonal Sale — Code: FALL25"
    ])

    st.write("🧾 Coupons being analyzed:")
    for coupon in coupons:
        st.write(f"- {coupon}")

    prompt = (
        f"You are an expert coupon analyst for {store_input}.com.\n"
        f"Here are the current coupons:\n" + "\n".join(coupons) +
        "\n\nPlease rank them by value and explain which one is best for customers shopping at this store."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        summary = response['choices'][0]['message']['content']
        st.write("✅ AI Summary of Coupons:")
        st.write(summary)
    except Exception as e:
        st.error(f"❌ Error calling OpenAI: {e}")

