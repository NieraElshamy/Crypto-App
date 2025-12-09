import streamlit as st
import pyperclip  # لازم تثبتها: pip install pyperclip

def show_history_page():
    st.set_page_config(page_title="History 📝", layout="wide", )
    #st.title("History of Encryption/Decryption 📝")
    st.markdown('<h1 style="text-align:center; color:#cc99ff; font-weight:700; margin-bottom:25px;">History of Encryption/Decryption 📝</h1>', unsafe_allow_html=True)

    if "history" not in st.session_state:
        st.session_state["history"] = []

    if not st.session_state["history"]:
        st.info("No history yet.")
        return

    # عمودين للكروت
    col1, col2 = st.columns(2)

    # ألوان لكل Algorithm
    algo_colors = {
        "AES": "#FFB74D",
        "RSA": "#64B5F6",
        "DNA": "#81C784",
        "Text": "#BA68C8",
        "File": "#90A4AE"
    }

    for idx, item in enumerate(reversed(st.session_state["history"])):
        col = col1 if idx % 2 == 0 else col2

        # اللون حسب Algorithm أو افتراضي
        color = algo_colors.get(item['algo'], "#4CAF50")

        # أيقونة حسب نوع العملية
        icon = "🔒" if item['action'] == "Encryption" else "🔓"

        card_html = f"""
        <div style="
            border:2px solid {color};
            border-radius:15px;
            padding:15px;
            margin-bottom:15px;
            background-color:#f9f9f9;
            box-shadow: 2px 2px 12px rgba(0,0,0,0.15);
            transition: transform 0.2s, box-shadow 0.2s;
        " onmouseover="this.style.transform='scale(1.02)'; this.style.boxShadow='4px 4px 20px rgba(0,0,0,0.25)';" onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='2px 2px 12px rgba(0,0,0,0.15)';">
            <h4 style="color:{color}; margin-bottom:5px;">{icon} {item['algo']} - {item['action']}</h4>
        </div>
        """
        col.markdown(card_html, unsafe_allow_html=True)

        with col.expander("View Details 🔍"):
            st.markdown("**Input:**")
            st.text_area(f"Input {idx}", item['input'], height=80, key=f"input_{idx}")
            if st.button(f"Copy Input {idx} 📋", key=f"copy_input_{idx}"):
                pyperclip.copy(item['input'])
                st.success("✅ Input copied to clipboard!")

            st.markdown("**Output:**")
            st.text_area(f"Output {idx}", item['output'], height=80, key=f"output_{idx}")
            if st.button(f"Copy Output {idx} 📋", key=f"copy_output_{idx}"):
                pyperclip.copy(item['output'])
                st.success("✅ Output copied to clipboard!")

    # زر لمسح التاريخ
    if st.button("Clear History 🗑️"):
        st.session_state["history"] = []  # مسح البيانات
        st.success("History cleared!")
        return  # فورًا يعيد رسم الصفحة بدون أي محتوى من الـ history
