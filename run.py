import pandas as pd
import streamlit as st

# 设置文件上传
st.title("Excel 数据填充")
uploaded_file = st.file_uploader("上传包含学生信息的 Excel 文件 (list.xlsx)", type=["xlsx"])

# 读取 student.xlsx 模板
template_path = 'template.xlsx'
students_df = pd.read_excel(template_path)

if uploaded_file is not None:
    # 读取用户上传的文件
    list_df = pd.read_excel(uploaded_file)

    # 根据“学号”更新“学生姓名”和“教师”列
    for index, row in students_df.iterrows():
        student_id = row['学号']
        match = list_df[list_df['学号'] == student_id]
        if not match.empty:
            students_df.at[index, '学生姓名'] = match['学生姓名'].values[0]
            students_df.at[index, '教师'] = match['教师'].values[0]

    # 输出更新后的 DataFrame
    st.write("更新后的学生信息：")
    st.dataframe(students_df)

    # 保存更新后的文件
    output_file = "updated_student.xlsx"
    students_df.to_excel(output_file, index=False)
    st.download_button("下载更新后的文件", output_file)
