import streamlit as st
import requests

# Cấu hình trang chuyên nghiệp
st.set_page_config(page_title="TikTok HD Downloader", page_icon="🎬", layout="centered")

# Giao diện tùy chỉnh bằng CSS
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f6; }
    .stButton>button {
        width: 100%;
        background-color: #eb4034;
        color: white;
        border-radius: 8px;
        height: 3em;
        font-size: 18px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover { background-color: #c23329; color: white; }
    .main-box {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 Hệ thống Tải Video HD")
st.write("Giải pháp lấy tư liệu thang máy sắc nét, không dính ID.")

# Tạo Form để có nút xác nhận (Enter)
with st.container():
    with st.form(key='download_form'):
        url = st.text_input("Dán link TikTok vào đây:", placeholder="https://www.tiktok.com/...")
        submit_button = st.form_submit_button(label='🚀 BẮT ĐẦU XỬ LÝ')

if submit_button and url:
    with st.spinner('⚙️ Đang bóc tách bản HD chất lượng cao...'):
        try:
            # Gọi API với tham số HD
            api_url = f"https://www.tikwm.com/api/?url={url}&hd=1"
            response = requests.get(api_url).json()
            
            if response.get('code') == 0:
                data = response['data']
                # Lấy link HD sắc nét nhất
                video_url = data.get('hdplay') or data.get('play')
                title = data.get('title', 'video_thang_may')
                
                st.success("✅ Đã xử lý thành công bản HD!")
                
                # Hiển thị Video Preview
                st.video(video_url)
                
                # Khu vực tải về chuyên nghiệp
                st.markdown(f"""
                    <div style="background-color: #e3f2fd; padding: 20px; border-radius: 12px; border: 1px solid #90caf9; text-align: center; margin-top: 20px;">
                        <p style="font-weight: bold; color: #1565c0; font-size: 18px;">📥 TẢI FILE GỐC SẮC NÉT</p>
                        <a href="{video_url}" target="_blank">
                            <button style="width: 100%; background-color: #1976d2; color: white; padding: 15px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 16px;">
                                MỞ VÀ LƯU VIDEO HD (TAB MỚI)
                            </button>
                        </a>
                        <p style="margin-top: 15px; font-size: 14px; color: #555; text-align: left;">
                            <b>Hướng dẫn lưu file:</b><br>
                            1. Sau khi tab mới mở ra, nhấn <b>Chuột phải</b> vào video.<br>
                            2. Chọn <b>"Lưu video thành..." (Save video as...)</b>.<br>
                            3. Mở file bằng <b>VLC</b> để thấy rõ từng chi tiết cơ khí/inox.
                        </p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.error("❌ Không lấy được link HD. Vui lòng kiểm tra lại link video.")
        except Exception as e:
            st.error(f"⚠️ Lỗi hệ thống: {e}")

st.divider()
st.caption("Công cụ được dựng bởi Mạnh Long")
