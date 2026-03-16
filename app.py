import streamlit as st
import yt_dlp

st.set_page_config(page_title="TikTok Downloader Pro", page_icon="🎬")

st.title("🎬 TikTok Downloader - Fix 403 Forbidden")
st.write("Giải pháp bóc tách link gốc để tránh bị TikTok chặn server.")

url = st.text_input("Dán link TikTok vào đây:")

if url:
    with st.spinner('⚙️ Đang bóc tách link trực tiếp...'):
        # Cấu hình tối giản để tránh bị nhận diện là bot
        ydl_opts = {
            'format': 'best',
            'quiet': True,
            'no_warnings': True,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                # Lấy link CDN trực tiếp từ TikTok
                video_url = info.get('url')
                
                if video_url:
                    st.success("✅ Đã tìm thấy link video gốc!")
                    
                    # 1. Hiển thị trình phát video (Nếu vẫn 0:00 thì đừng lo, quan trọng là link tải)
                    st.video(video_url)
                    
                    # 2. Tạo nút mở link trực tiếp
                    st.markdown(f"""
                        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border: 1px solid #ddd;">
                            <p><b>Bước 1:</b> Nhấn vào nút xanh dưới đây để mở video ở tab mới.</p>
                            <a href="{video_url}" target="_blank">
                                <button style="width: 100%; background-color: #28a745; color: white; padding: 15px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 16px;">
                                    MỞ VIDEO TRONG TAB MỚI
                                </button>
                            </a>
                            <p style="margin-top: 15px;"><b>Bước 2:</b> Tại tab mới, bạn nhấn <b>chuột phải</b> vào video và chọn <b>"Lưu video thành..." (Save video as...)</b>.</p>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error("Không thể trích xuất link. Video có thể ở chế độ riêng tư.")
                    
        except Exception as e:
            st.error(f"Lỗi hệ thống: {e}")

st.info("💡 Vì bạn đã có VLC, sau khi tải về bạn cứ mở bằng VLC là sẽ thấy nội dung video cực nét!")
