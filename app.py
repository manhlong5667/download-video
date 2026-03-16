import streamlit as st
import requests

st.set_page_config(page_title="TikTok Downloader Pro", page_icon="🎬")

st.title("🎬 TikTok Downloader - Bản Sửa Lỗi 403")
st.write("Giải pháp lấy tư liệu thang máy qua cổng dự phòng.")

url = st.text_input("Dán link TikTok vào đây:")

if url:
    with st.spinner('⚙️ Đang xử lý qua cổng dự phòng...'):
        try:
            # Sử dụng API trung gian để bóc tách link gốc, tránh bị chặn IP
            api_url = f"https://www.tikwm.com/api/?url={url}"
            response = requests.get(api_url).json()
            
            if response.get('code') == 0:
                data = response['data']
                video_url = data['play'] # Link video không dính ID
                title = data.get('title', 'video_thang_may')
                
                st.success("✅ Đã lấy được video!")
                
                # Hiển thị video để xem trước
                st.video(video_url)
                
                # Nút tải trực tiếp từ trình duyệt của bạn
                st.markdown(f"""
                    <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border: 1px solid #ddd;">
                        <p style="font-weight: bold; color: #2e7d32;">CÁCH TẢI CHẮC CHẮN THÀNH CÔNG:</p>
                        <a href="{video_url}" target="_blank">
                            <button style="width: 100%; background-color: #2e7d32; color: white; padding: 15px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 16px;">
                                📥 MỞ VÀ TẢI VIDEO (TAB MỚI)
                            </button>
                        </a>
                        <p style="margin-top: 15px; font-size: 14px;">
                            Sau khi nhấn, video hiện ra ở tab mới -> <b>Chuột phải</b> -> <b>Lưu video thành...</b> -> Mở bằng <b>VLC</b>.
                        </p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.error("Không bóc tách được link. Thử lại với link khác.")
        except Exception as e:
            st.error(f"Lỗi kết nối: {e}")

st.info("💡 Cách này không dùng server Streamlit để tải nên sẽ thoát được lỗi 403 Forbidden.")
