import streamlit as st
import yt_dlp
import requests

# Cấu hình giao diện
st.set_page_config(page_title="TikTok Pro Downloader", page_icon="🎬")

st.title("🎬 TikTok Downloader - Max Quality")
st.write("Đã tối ưu để xem bằng VLC - Chất lượng gốc, không ID.")

url = st.text_input("Dán link TikTok tại đây:")

if url:
    with st.spinner('🚀 Đang lấy video chất lượng cao nhất...'):
        # Cấu hình lấy bản ĐẸP NHẤT, không quan tâm định dạng vì đã có VLC
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best', # Lấy cái tốt nhất hiện có
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
                    # Dùng requests để lấy dữ liệu thực tránh file vài Bytes
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                    }
                    response = requests.get(video_url, headers=headers, stream=True)
                    video_bytes = response.content
                    
                    if len(video_bytes) > 1000: # Kiểm tra nếu dung lượng lớn hơn 1KB
                        st.success(f"✅ Đã sẵn sàng! Dung lượng: {len(video_bytes)/(1024*1024):.2f} MB")
                        
                        # Preview (Nếu trình duyệt không đọc được HEVC thì phần này sẽ đen, nhưng nút tải vẫn OK)
                        st.video(video_bytes)
                        
                        # Nút tải xuống
                        st.download_button(
                            label="📥 TẢI VIDEO GỐC (DÙNG VLC ĐỂ XEM)",
                            data=video_bytes,
                            file_name=f"{title}.mp4",
                            mime="video/mp4"
                        )
                    else:
                        st.error("❌ Lỗi dữ liệu: File nhận được quá nhỏ. Hãy thử Reboot App hoặc đổi link.")
                        
        except Exception as e:
            st.error(f"⚠️ Lỗi: {e}")

st.markdown("---")
st.caption("Gợi ý: Nhấn chuột phải vào file vừa tải > Open with > VLC media player.")
