import streamlit as st
import requests

# 获取Edge TTS可用语音
def get_edge_tts_voices():
    url = "https://edge.microsoft.com/tts/voices"
    response = requests.get(url)
    return response.json()

def main():
    st.title("Edge TTS 语音列表")
    
    voices = get_edge_tts_voices()
    
    if voices:
        st.header("可用的语音")
        
        for voice in voices:
            language = voice['locale']
            name = voice['name']
            st.write(f"语言: {language}, 语音: {name}")
    else:
        st.write("未找到可用语音。")

if __name__ == "__main__":
    main()
