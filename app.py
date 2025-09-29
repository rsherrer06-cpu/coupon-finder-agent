import streamlit as st

st.title("🤑 Coupon Finder AI Agent")

store = st.text_input("Enter store name (e.g., nike)")

if st.button("Find Coupons") and store:
    st.write(f"🔍 Searching for coupons for {store}.com...")
    st.write("✅ Coupons Found:")
    st.write("- 20% Off Sitewide — Code: NIKE20")
    st.write("- Free Shipping Over $50 — Code: SHIPFREE")
    st.write("- Buy 1 Get 1 50% Off — Code: BOGO50")
