import streamlit as st
import yt_dlp

# Cấu hình giao diện chuyên nghiệp
st.set_page_config(page_title="TikTok Downloader Pro", page_icon="🎬")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 TikTok Downloader Pro")
st.write("Phiên bản sửa lỗi 403 Forbidden & Video 0:00 cho tư liệu kỹ thuật.")

url = st.text_input("Dán link video TikTok vào đây:", placeholder="https://www.tiktok.com/...")

if url:
    with st.spinner('⚙️ Đang bóc tách luồng dữ liệu gốc...'):
        # Cấu hình giả lập thiết bị di động để TikTok không chặn
        ydl_opts = {
            'format': 'best',
            'quiet': True,
            'no_warnings': True,
            'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                video_url = info.get('url')
                title = info.get('title', 'video_tiktok')
                
                if video_url:
                    st.success("✅ Đã lấy được link gốc từ TikTok!")
                    
                    # Hiển thị trình phát video (Nếu vẫn 0:00 là do lỗi Codec trình duyệt, hãy cứ tải về)
                    st.video(video_url)
                    
                    st.info("💡 Mẹo: Nếu video trên báo 0:00, hãy dùng nút tải bên dưới và mở bằng VLC.")

                    # NÚT TẢI CƯỠNG BỨC: Ép trình duyệt của bạn tự tải, bỏ qua server Streamlit
                    st.markdown(f"""
                        <div style="background-color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #e0e0e0; text-align: center;">
                            <p style="color: #d32f2f; font-weight: bold;">CÁCH TẢI ĐỂ CÓ NỘI DUNG (VƯỢT LỖI 403):</p>
                            <a href="{video_url}" target="_blank" rel="noopener noreferrer">
                                <button style="width: 100%; background-color: #2e7d32; color: white; padding: 15px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 16px;">
                                    📥 NHẤN VÀO ĐÂY ĐỂ MỞ TAB TẢI VIDEO
                                </button>
                            </a>
                            <div style="text-align: left; margin-top: 15px; font-size: 14px; color: #616161;">
                                <b>Sau khi nhấn nút:</b><br>
                                1. Một tab mới sẽ mở ra chỉ chứa video.<br>
                                2. Bạn nhấn <b>Chuột phải</b> vào video đó.<br>
                                3. Chọn <b>"Lưu video thành..." (Save video as...)</b>.<br>
                                4. Khi tải xong, hãy mở file bằng <b>VLC</b>.
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error("❌ Không tìm thấy link video trực tiếp.")
                    
        except Exception as e:
            st.error(f"⚠️ Lỗi bóc tách: {str(e)}")
            st.info("Thử Reboot App trên Streamlit nếu lỗi này lặp lại.")

st.divider()
st.caption("Công cụ hỗ trợ lưu trữ tư liệu thang máy không dính ID.")
