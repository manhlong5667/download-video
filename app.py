import streamlit as st
import yt_dlp

st.set_page_config(page_title="TikTok Downloader Pro", page_icon="🎬")

st.title("🎬 TikTok Downloader Pro")
st.write("Giải pháp tải tư liệu kỹ thuật không dính ID (Dự phòng đa cổng)")

url = st.text_input("Dán link TikTok vào đây:", placeholder="https://www.tiktok.com/...")

if url:
    with st.spinner('⚙️ Đang bóc tách luồng dữ liệu...'):
        ydl_opts = {
            'format': 'best',
            'quiet': True,
            'no_warnings': True,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                direct_url = info.get('url')
                title = info.get('title', 'video_thang_may')
                
                if direct_url:
                    st.success("✅ Đã lấy được link gốc!")
                    
                    # Hiển thị video trực tiếp trên web
                    st.video(direct_url)
                    
                    st.markdown("### 📥 Chọn cổng tải về:")
                    
                    # CỔNG 1: Tải trực tiếp (Dành cho trình duyệt Edge/Chrome)
                    st.markdown(f"""
                        <a href="{direct_url}" target="_blank" download="{title}.mp4">
                            <button style="width: 100%; background-color: #007bff; color: white; padding: 12px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; margin-bottom: 10px;">
                                CỔNG 1: Tải trực tiếp (Khuyên dùng)
                            </button>
                        </a>
                    """, unsafe_allow_html=True)
                    
                    # CỔNG 2: Mở video ở tab mới để "Save video as..."
                    st.markdown(f"""
                        <a href="{direct_url}" target="_blank">
                            <button style="width: 100%; background-color: #28a745; color: white; padding: 12px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer;">
                                CỔNG 2: Mở tab mới (Chuột phải > Lưu video)
                            </button>
                        </a>
                    """, unsafe_allow_html=True)

                    st.warning("⚠️ Nếu Cổng 1 tải về file vài KB, hãy dùng Cổng 2: Đợi video hiện ra ở tab mới -> Chuột phải -> chọn 'Lưu video thành...'")
                
        except Exception as e:
            st.error(f"Lỗi: {e}")

st.divider()
st.info("💡 Mẹo: Vì bạn đã cài VLC, cứ thấy file tải về là MP4 hay MKV thì VLC đều cân được hết!")
