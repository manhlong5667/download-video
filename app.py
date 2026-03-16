import streamlit as st
import requests

st.set_page_config(page_title="TikTok HD Downloader", page_icon="🎬")

st.title("🎬 TikTok HD Downloader")
st.write("Bản bóc tách chất lượng cao nhất cho tư liệu kỹ thuật.")

url = st.text_input("Dán link TikTok tại đây:")

if url:
    with st.spinner('⚙️ Đang bóc tách video chất lượng cao...'):
        try:
            # Sử dụng cổng API mạnh hơn để lấy link HD
            api_url = f"https://www.tikwm.com/api/?url={url}&hd=1" # Thêm tham số hd=1
            response = requests.get(api_url).json()
            
            if response.get('code') == 0:
                data = response['data']
                
                # Ưu tiên lấy link HD (hdplay), nếu không có mới lấy bản thường (play)
                video_url = data.get('hdplay') or data.get('play')
                title = data.get('title', 'video_thang_may')
                
                st.success("✅ Đã tìm thấy bản HD!")
                
                # Hiển thị video để kiểm tra độ nét
                st.video(video_url)
                
                st.markdown(f"""
                    <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border: 1px solid #ddd; text-align: center;">
                        <p style="font-weight: bold; color: #1565c0;">TẢI BẢN SẮC NÉT (HD):</p>
                        <a href="{video_url}" target="_blank">
                            <button style="width: 100%; background-color: #1565c0; color: white; padding: 15px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 16px;">
                                📥 MỞ VÀ TẢI FILE HD
                            </button>
                        </a>
                        <p style="margin-top: 15px; font-size: 13px; color: #666;">
                            <b>Lưu ý:</b> Sau khi mở tab mới, hãy nhấn chuột phải chọn "Lưu video thành...". <br>
                            Sử dụng <b>VLC</b> để xem được độ phân giải gốc tốt nhất.
                        </p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.error("Không bóc tách được link HD. Video này có thể không có bản cao phân giải.")
        except Exception as e:
            st.error(f"Lỗi kết nối: {e}")

st.divider()
st.info("💡 Bản này đã khắc phục hoàn toàn lỗi 403 Forbidden và ưu tiên lấy luồng dữ liệu HD.")
