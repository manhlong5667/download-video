import streamlit as st
import yt_dlp

st.set_page_config(page_title="TikTok Downloader Pro", page_icon="🎬")

st.title("🎬 TikTok Video Downloader")
st.write("Giải pháp lấy tư liệu kỹ thuật & thang máy không dính ID.")

url = st.text_input("Dán link TikTok vào đây:", placeholder="https://www.tiktok.com/...")

if url:
    with st.spinner('⚙️ Đang bóc tách luồng dữ liệu gốc...'):
        ydl_opts = {
            'format': 'best',
            'quiet': True,
            'no_warnings': True,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                video_url = info.get('url')
                title = info.get('title', 'video_thang_may')
                
                if video_url:
                    st.success("✅ Đã tìm thấy luồng video!")
                    
                    # 1. Nút tải trực tiếp (Dành cho trình duyệt hiện đại)
                    st.markdown(f"""
                        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border: 1px solid #ddd; text-align: center;">
                            <p style="color: #333; font-weight: bold;">CÁCH TẢI CHẮC CHẮN THÀNH CÔNG:</p>
                            <a href="{video_url}" target="_blank">
                                <button style="width: 100%; background-color: #ff4b4b; color: white; padding: 15px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 18px;">
                                    🚀 MỞ VIDEO VÀ TẢI VỀ
                                </button>
                            </a>
                            <div style="text-align: left; margin-top: 15px; font-size: 14px; color: #555;">
                                <b>Hướng dẫn sau khi bấm nút:</b><br>
                                1. Video sẽ mở ở một tab mới.<br>
                                2. Bạn nhấn <b>Chuột phải</b> vào video đó.<br>
                                3. Chọn <b>"Lưu video thành..." (Save video as...)</b>.<br>
                                4. Mở file vừa tải bằng <b>VLC</b> để xem nội dung.
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error("Không thể lấy được link trực tiếp từ video này.")
                    
        except Exception as e:
            st.error(f"Lỗi: {e}")

st.divider()
st.info("💡 Lưu ý: Trình duyệt có thể hiện video 0:00 hoặc màn hình đen do thiếu Codec HEVC, nhưng khi bạn 'Lưu video thành...' thì file tải về sẽ có đầy đủ nội dung.")
