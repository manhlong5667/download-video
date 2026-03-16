import streamlit as st
import yt_dlp
import os
import requests

# Cấu hình giao diện trang web
st.set_page_config(page_title="Tải Video TikTok Không ID", page_icon="🎬", layout="centered")

# CSS để làm nút bấm đẹp hơn
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 TikTok Video Downloader")
st.subheader("Dành cho tư liệu thang máy & kỹ thuật")

# Ô nhập link
url = st.text_input("Dán link TikTok vào đây:", placeholder="https://www.tiktok.com/@user/video/...")

if url:
    with st.spinner('⚙️ Đang bóc tách dữ liệu từ TikTok...'):
        # Cấu hình yt-dlp thông minh hơn
        ydl_opts = {
            # Thử lấy H.264 (avc1) trước để Windows đọc được, nếu không có thì lấy bản tốt nhất bất kỳ
            'format': 'bestvideo[vcodec^=avc1]+bestaudio[acodec^=mp4a]/best[vcodec^=avc1]/best',
            'quiet': True,
            'no_warnings': True,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # Lấy thông tin video
                info = ydl.extract_info(url, download=False)
                video_url = info.get('url')
                title = info.get('title', 'video_tiktok')
                
                if video_url:
                    st.success("✅ Đã tìm thấy video!")
                    
                    # Hiển thị video để xem trước (Preview)
                    st.video(video_url)
                    
                    # Xử lý luồng tải xuống thực tế (để tránh lỗi 403 khi nhấn nút)
                    response = requests.get(video_url, stream=True)
                    video_bytes = response.content

                    # Nút bấm tải về máy
                    st.download_button(
                        label="🚀 TẢI VIDEO VỀ MÁY (KHÔNG ID)",
                        data=video_bytes,
                        file_name=f"{title}.mp4",
                        mime="video/mp4"
                    )
                    
                    st.info("💡 Mẹo: Nếu video tải về không có tiếng, hãy cài thêm ffmpeg vào project của bạn.")
                else:
                    st.error("❌ Không thể lấy link trực tiếp từ video này.")
                    
        except Exception as e:
            st.error(f"⚠️ Lỗi hệ thống: {str(e)}")
            st.warning("Thử lại với link khác hoặc kiểm tra xem video có bị xóa không.")

st.markdown("---")
st.caption("Công cụ hỗ trợ tải tư liệu kỹ thuật nhanh chóng.")
