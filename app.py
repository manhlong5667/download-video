import streamlit as st
import yt_dlp

st.set_page_config(page_title="TikTok Downloader Pro", page_icon="⚡")

st.title("⚡ TikTok Downloader Pro")
st.write("Phiên bản sửa lỗi 'File quá nhỏ' - Tải trực tiếp từ máy chủ TikTok.")

url = st.text_input("Dán link TikTok vào đây:")

if url:
    with st.spinner('🔍 Đang lấy link gốc...'):
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'quiet': True,
            'no_warnings': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                # Lấy link trực tiếp từ TikTok
                direct_url = info.get('url')
                title = info.get('title', 'video_tiktok')
                
                if direct_url:
                    st.success("✅ Đã lấy link thành công!")
                    
                    # Hiển thị video để xem trước
                    st.video(direct_url)
                    
                    # Nút bấm dùng HTML để kích hoạt trình duyệt của BẠN tự tải về
                    # Cách này giúp vượt qua việc server Streamlit bị chặn
                    st.markdown(f"""
                        <a href="{direct_url}" target="_blank" download="{title}.mp4">
                            <button style="
                                width: 100%;
                                background-color: #ff4b4b;
                                color: white;
                                padding: 15px;
                                border: none;
                                border-radius: 10px;
                                font-weight: bold;
                                cursor: pointer;
                                font-size: 18px;
                            ">
                                📥 BẤM VÀO ĐÂY ĐỂ TẢI VIDEO
                            </button>
                        </a>
                        <br><br>
                        <p style="color: #666; font-size: 14px;">
                            <b>Lưu ý quan trọng:</b> Nếu nhấn nút mà video chỉ hiện ra để xem: <br>
                            1. Nhấn vào <b>dấu 3 chấm</b> ở góc dưới video. <br>
                            2. Chọn <b>Tải xuống (Download)</b>.
                        </p>
                    """, unsafe_allow_html=True)
                else:
                    st.error("Không tìm thấy link video gốc.")
        except Exception as e:
            st.error(f"Lỗi: {e}")

st.divider()
st.caption("Mẹo: Đã có VLC thì bạn cứ tải bản cao nhất này về xem cho nét!")
