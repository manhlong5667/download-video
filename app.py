import streamlit as st
import yt_dlp
import requests
import io

# 1. Cấu hình giao diện trang web
st.set_page_config(
    page_title="TikTok Downloader - No ID", 
    page_icon="🎬", 
    layout="centered"
)

# Thêm một chút CSS để giao diện sạch sẽ, chuyên nghiệp hơn
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3.5em;
        background-color: #00ADFF;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0087c7;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 TikTok Video Downloader")
st.write("Tải video TikTok không dính ID - Hỗ trợ tư liệu kỹ thuật & thang máy.")

# 2. Ô nhập link video
url = st.text_input("Dán link video TikTok vào đây:", placeholder="https://www.tiktok.com/...")

if url:
    with st.spinner('⚙️ Đang bóc tách dữ liệu... Vui lòng đợi trong giây lát.'):
        # Cấu hình yt-dlp cực kỳ linh hoạt (Dòng này quan trọng nhất)
        ydl_opts = {
            # Thử lấy H.264 (avc1) trước, nếu không có thì lấy bản tốt nhất bất kỳ
            'format': 'bestvideo[vcodec^=avc1]+bestaudio[acodec^=mp4a]/bestvideo+bestaudio/best',
            'quiet': True,
            'no_warnings': True,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # Trích xuất thông tin
                info = ydl.extract_info(url, download=False)
                video_url = info.get('url')
                title = info.get('title', 'video_tiktok')
                
                if video_url:
                    st.success("✅ Đã tìm thấy video!")
                    
                    # Hiển thị video xem trước
                    st.video(video_url)
                    
                    # Xử lý tải dữ liệu video về RAM của server để người dùng tải về máy (Tránh lỗi 403)
                    try:
                        video_data = requests.get(video_url, stream=True).content
                        
                        # Nút bấm tải xuống
                        st.download_button(
                            label="📥 TẢI VIDEO XUỐNG MÁY",
                            data=video_data,
                            file_name=f"{title}.mp4",
                            mime="video/mp4"
                        )
                        st.info("💡 Lưu ý: Nếu video tải về không xem được bằng trình duyệt, hãy dùng phần mềm VLC.")
                    except:
                        st.error("Không thể tải dữ liệu video. Vui lòng thử lại hoặc dùng link khác.")
                else:
                    st.error("❌ Không lấy được link video trực tiếp.")
                    
        except Exception as e:
            st.error(f"⚠️ Lỗi: {str(e)}")
            st.info("Mẹo: Đảm bảo bạn dán đúng link video TikTok (có chữ /video/ trong link).")

st.markdown("---")
st.caption("Công cụ hỗ trợ lưu trữ tư liệu chuyên dụng.")
