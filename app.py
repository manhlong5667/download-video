import streamlit as st
import yt_dlp

st.set_page_config(page_title="TikTok Downloader Pro", page_icon="⚡")

st.title("⚡ TikTok Downloader - Fix 403")
st.write("Sửa lỗi Forbidden và Video không có nội dung.")

url = st.text_input("Dán link TikTok vào đây:")

if url:
    with st.spinner('🔍 Đang bóc tách luồng video...'):
        # Cấu hình lấy link gốc không qua trung gian
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'quiet': True,
            'no_warnings': True,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                direct_url = info.get('url')
                title = info.get('title', 'video_tiktok')
                
                if direct_url:
                    st.success("✅ Đã tìm thấy luồng video gốc!")
                    
                    # Hiển thị video để kiểm tra
                    st.video(direct_url)
                    
                    # NÚT BẤM THẦN THÁNH: Ép trình duyệt tự tải luồng gốc
                    # Cách này giúp máy tính của bạn tự kết nối với TikTok, bỏ qua server Streamlit bị chặn
                    st.markdown(f"""
                        <div style="text-align: center;">
                            <a href="{direct_url}" target="_blank" rel="noopener noreferrer">
                                <button style="
                                    width: 100%;
                                    background-color: #25D366;
                                    color: white;
                                    padding: 20px;
                                    border: none;
                                    border-radius: 15px;
                                    font-weight: bold;
                                    font-size: 20px;
                                    cursor: pointer;
                                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                                ">
                                    📥 NHẤN VÀO ĐÂY ĐỂ MỞ FILE GỐC
                                </button>
                            </a>
                            <p style="margin-top: 15px; color: #555;">
                                <b>Hướng dẫn:</b> Sau khi nhấn nút, nếu video hiện ra ở tab mới: <br>
                                Chuột phải vào video -> Chọn <b>"Lưu video thành..." (Save video as...)</b>
                            </p>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error("Không lấy được link trực tiếp.")
        except Exception as e:
            st.error(f"Lỗi bóc tách: {e}")

st.divider()
st.info("Vì bạn đã có VLC, file tải về dù là định dạng nào cũng sẽ xem được cực nét.")
