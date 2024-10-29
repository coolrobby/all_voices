import streamlit as st
import requests

# 获取Edge TTS可用语音
def get_edge_tts_voices():
    url = "https://edge.microsoft.com/tts/voices"
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP错误: {http_err}")
    except requests.exceptions.RequestException as req_err:
        st.error(f"请求错误: {req_err}")
    except ValueError:
        st.error("返回的数据无法解析为JSON格式。")
    
    return []

def main():
    st.title("Edge TTS 语音列表")
    
    voices = get_edge_tts_voices()
    
    if voices:
        st.header("可用的语音")
        
        for voice in voices:
            language = voice.get('locale', '未知语言')
            name = voice.get('name', '未知语音')
            st.write(f"语言: {language}, 语音: {name}")
    else:
        st.write("未找到可用语音。")

if __name__ == "__main__":
    main()
