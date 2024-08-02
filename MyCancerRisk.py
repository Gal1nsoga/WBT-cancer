# 代码目的：基于streamlit包生成网页

# 导入包
import pandas as pd
import streamlit as st
import joblib
import pickle

# main function
# 设置网页名称
st.set_page_config(page_title='MyCancerRisk癌症风险预测工具')


# 设置网页标题
st.header('Cancer risk assessment web tool for middle-aged and older adults\n中老年人癌症风险评估网页工具')

# 设置副标题
st.subheader('Welcome to use this tool! Please enter the following information to make a prediction:\n欢迎使用本工具！请您输入以下信息进行预测：')

# 在侧边栏添加图片
# st.sidebar.image('https://cdn.freebiesupply.com/logos/thumbs/1x/nvidia-logo.png', width=200)

# st.title('请您输入以下信息：')

# 在侧边栏添加说明
st.sidebar.info(
    "You can use this tool to predict the likelihood of cancer now. Please note that this forecast is for reference only and the actual results are subject to the doctor's examination results.\n您可使用本工具预测现在癌症的可能性。请注意，本预测结果仅供参考，实际结果需以医生检查结果为准。")

# Function for online predictions
# 在侧边栏输入预测因子
# 添加滑动条
# factor1 = st.sidebar.selectbox(
#       'Age',
#        ('<50', '50-64', '>=65')
#    )  # 显示列表选择框

# 填写预测变量
# 社会人口学
factor1 = st.radio('Residence Type (户口类型)', ['Agricultural Type(农业户口)', 'None-Agricultural Type (非农户口)', 'Unified Residence Type (统一居民户口)', 'Unclear (不清楚)'], index = None)
factor2 = st.radio('Education Level (教育水平)', ['Elementary school or below (小学及以下)', 'Junior high school graduate (初中毕业)', 'High school or vocational school graduate (高中或中专毕业)', 'College diploma graduate (大专毕业)', 'Bachelors degree or above (本科及以上)', 'Unclear (不清楚)'], index = None)
factor3 = st.radio('Marital Status( 婚姻状态)', ['Married (已婚)', 'Single (未婚)', 'Divorced or widowed (离异或丧偶)', 'Unclear (不清楚)'], index = None)
factor4 = st.radio('Gender (性别)', ['Male (男性)', 'Female (女性)'], index = None)
factor5 = st.slider('Age (请选择您的年龄)', 45, 120)
factor6 = st.slider('Night Sleep Druation (您晚上的睡眠时间)', 0, 24)
factor7 = st.radio('How many meals do you eat every day？(您每日吃几顿饭？)', ['Four or more meals per day (每天大于等于四顿)', 'Three meals per day (每天三顿)', 'Two meals per day (每天两顿)', 'One meal per day (每天一顿)', 'Unclear (不清楚)'], index = None)
factor8 = st.radio('Alcohol consumption frequency in a year (您一年内喝酒频率)', ['More than once a month (每个月超过一次)', 'Once or less a month (每月少于等于一次)', 'Do not drink (不喝)', 'Unclear (不清楚)'], index = None)
factor9 = st.radio('Do you have chest pain on the left side? (您是否左胸痛？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor10 = st.radio('Do you have hypertension? (您是否有高血压？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor11 = st.radio('Do you have dyslipidemia? (您是否有血脂异常？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor12 = st.radio('Do you have diabetes? (您是否有糖尿病？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor13 = st.radio('Do you have chronic lung disease? (您是否有慢性肺部疾病？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor14 = st.radio('Do you have liver disease? (您是否有肝脏疾病？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor15 = st.radio('Do you have heart attack? (您是否有心脏病？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor16 = st.radio('Do you have stroke? (您是否有中风？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor17 = st.radio('Do you have kidney disease? (您是否有肾脏疾病？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor18 = st.radio('Do you have gastric or digestive disease? (您是否有胃部或消化系统疾病？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor19 = st.radio('Do you have emotional or mental issue? (您是否有情感及精神方面问题？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor20 = st.radio('Do you have memory-related diseases? (您是否有与记忆相关疾病？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor21 = st.radio('Do you have arthritis or rheumatism? (您是否有关节炎或风湿？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor22 = st.radio('Do you have asthma? (您是否有哮喘？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor23 = st.radio('Have you experienced a traffic accident or a major injury accident? (您是否有经历过交通事故或重大意外伤害？)', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor24 = st.radio('Have you been diagnosed with glaucoma? （您是否有确诊青光眼？）', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor25 = st.radio("How's your hearing? (您的听力如何？)", ['Very Good (非常好)', 'Good (很好)', 'Fair (好)', 'Average (一般)', 'Poor (不好)', 'Unclear (不清楚)'], index = None)
factor26 = st.radio('Have all your teeth fallen out? （您是否牙齿已经掉光？）', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor27 = st.radio('Do you often experience body pain? （您是否经常身体疼痛？）', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor28 = st.radio('Have you experienced a weight change of more than 5 kg within the past year?您是否一年内体重变化超过10斤？', ['Yes (是)', 'No (否)', 'Unclear (不清楚)'], index = None)
factor29 = st.radio('How was your nutrition during childhood? （您小时候的营养情况如何？）', ['Very Good (非常好)', 'Good (很好)', 'Fair (好)', 'Average (一般)', 'Poor (不好)', 'Unclear (不清楚)'], index = None)
factor30 = st.radio("How's your life quality? (您的生活水平如何？)", ['Very Good (非常好)', 'Good (很好)', 'Fair (好)', 'Average (一般)', 'Poor (不好)', 'Unclear (不清楚)'], index = None)
factor31 = st.radio("What's yuor work? (您的工作单位是？)", ['Government departments or public institutions (政府部门或事业单位)', 'Non-profit organizations and businesses (非盈利结构和企业)', 'Individual households, farmers, residential households (个体户农户居民户)', 'Others (其他)', 'Unclear (不清楚)'], index = None)
factor32 = st.radio('What type of the bathing facilities at your house? (您家里的洗澡设施是什么样的？)', ['Centralized hot water supply (统一供热水)', 'Household-installed water heater (家庭自装热水器)', 'No bathing facilities (没有洗澡设施)', 'Unclear (不清楚)'], index = None)
factor33 = st.radio('What type of the heating system facilities at your home? (您家里的供暖设施是什么样的？)', ['Solar energy (太阳能)', 'Coal or briquettes (煤炭或者蜂窝煤)', 'Piped natural gas (管道天然气或煤气)', 'Liquefied petroleum gas (LPG) (液化石油气)', 'Electricity (电)', 'Burning straw, firewood (烧秸秆、柴火)', 'Others (其他)', 'Unclear (不清楚)'], index = None)
factor34 = st.radio('How clean is the interior of your home? (您家里的室内整洁度如何？)', ['Very clean (非常整洁)', 'Quite clean (很整洁)', 'Clean (整洁)', 'Average (一般)', 'Unclean (不整洁)', 'Unclear (不清楚)'], index = None)
factor35 = st.radio('How would you rate your own health? （您对自己的健康评价如何？）', ['Very Good (非常好)', 'Good (很好)', 'Fair (好)', 'Average (一般)', 'Poor (不好)', 'Unclear (不清楚)'], index = None)
factor36 = st.radio("How's your smoking status? (您的吸烟状态是如何的？)", ['Currently smoking (目前吸烟)', 'Quit smoking (已经戒烟)', 'Never smoke (从不吸烟)', 'Unclear (不清楚)'], index = None)

# 创建dataframe，用于预测
input_dict = {'bc001': factor1, 'bd001': factor2, 'be001': factor3, 'rgender': factor4,
              'age_cul': factor5, 'da049': factor6, 'da058': factor7,
              'da067': factor8, 'da003': factor9, 'da007_1_': factor10, 'da007_2_': factor11,
              'da007_3_': factor12, 'da007_5_': factor13, 'da007_6_': factor14, 'da007_7_': factor15,
              'da007_8_': factor16, 'da007_9_': factor17, 'da007_10_': factor18, 'da007_11_': factor19,
              'da007_12_': factor20, 'da007_13_': factor21, 'da007_14_': factor22, 'da021': factor23,
              'da037': factor24, 'da039': factor25, 'da040': factor26, 'da041': factor27, 'da047': factor28,
              'da048': factor29, 'g003': factor30, 'fb002': factor31, 'i018': factor32,
              'i021': factor33, 'i025': factor34, 'Self-rated health': factor35, 'Smoke status': factor36
              }
input_df = pd.DataFrame([input_dict])


# 对dataframe中传入的数据进行编码
def codeing_fun(input_df):
    # 社会人口学
    input_df['bc001'] = input_df['bc001'].replace(['Agricultural Type(农业户口)', 'None-Agricultural Type (非农户口)', 'Unified Residence Type (统一居民户口)', 'Unclear (不清楚)'], [1, 2, 3, -1])
    input_df['bd001'] = input_df['bd001'].replace(['Elementary school or below (小学及以下)', 'Junior high school graduate (初中毕业)', 'High school or vocational school graduate (高中或中专毕业)', 'College diploma graduate (大专毕业)', 'Bachelors degree or above (本科及以上)', 'Unclear (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['be001'] = input_df['be001'].replace(['Married (已婚)', 'Single (未婚)', 'Divorced or widowed (离异或丧偶)', 'Unclear (不清楚)'], [1, 2, 3, -1])
    input_df['rgender'] = input_df['rgender'].replace(['Male (男性)', 'Female (女性)'], [1, 2])
    input_df['da058'] = input_df['da058'].replace(['Four or more meals per day (每天大于等于四顿)', 'Three meals per day (每天三顿)', 'Two meals per day (每天两顿)', 'One meal per day (每天一顿)', 'Not Sure (不清楚)'], [1, 3, 4, 5, -1])
    input_df['da067'] = input_df['da067'].replace(['More than once a month (每个月超过一次)', 'Once or less a month (每月少于等于一次)', 'Do not drink (不喝)', 'Unclear (不清楚)'], [1, 2, 3, -1])
    input_df['da003'] = input_df['da003'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da007_1_'] = input_df['da007_1_'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da007_2_'] = input_df['da007_2_'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da007_3_'] = input_df['da007_3_'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da007_5_'] = input_df['da007_5_'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da007_6_'] = input_df['da007_6_'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da007_7_'] = input_df['da007_7_'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da007_8_'] = input_df['da007_8_'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da007_9_'] = input_df['da007_9_'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da007_10_'] = input_df['da007_10_'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da007_11_'] = input_df['da007_11_'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da007_12_'] = input_df['da007_12_'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da007_13_'] = input_df['da007_13_'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da007_14_'] = input_df['da007_14_'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da021'] = input_df['da021'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da037'] = input_df['da037'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da039'] = input_df['da039'].replace(['Very Good (非常好)', 'Good (很好)', 'Fair (好)', 'Average (一般)', 'Poor (不好)', 'Not Sure (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['da040'] = input_df['da040'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da041'] = input_df['da041'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da047'] = input_df['da047'].replace(['Yes (是)', 'No (否)', 'Unclear (不清楚)'], [1, 2, -1])
    input_df['da048'] = input_df['da048'].replace(['Very Good (非常好)', 'Good (很好)', 'Fair (好)', 'Average (一般)', 'Poor (不好)', 'Not Sure (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['g003'] = input_df['g003'].replace(['Very Good (非常好)', 'Good (很好)', 'Fair (好)', 'Average (一般)', 'Poor (不好)', 'Not Sure (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['fb002'] = input_df['fb002'].replace(['Government departments or public institutions (政府部门或事业单位)', 'Non-profit organizations and businesses (非盈利结构和企业)', 'Individual households, farmers, residential households (个体户农户居民户)', 'Others (其他)', 'Unclear (不清楚)'], [1, 2, 3, 4, -1])
    input_df['i018'] = input_df['i018'].replace(['Centralized hot water supply (统一供热水)', 'Household-installed water heater (家庭自装热水器)', 'No bathing facilities (没有洗澡设施)', 'Unclear (不清楚)'], [1, 2, 3, -1])
    input_df['i021'] = input_df['i021'].replace(['Solar energy (太阳能)', 'Coal or briquettes (煤炭或者蜂窝煤)', 'Piped natural gas (管道天然气或煤气)', 'Liquefied petroleum gas (LPG) (液化石油气)', 'Electricity (电)', 'Burning straw, firewood (烧秸秆、柴火)', 'Others (其他)', 'Not Sure (不清楚)'], [1, 2, 3, 4, 5, 6, 7, -1])
    input_df['i025'] = input_df['i025'].replace(['Very clean (非常整洁)', 'Quite clean (很整洁)', 'Clean (整洁)', 'Average (一般)', 'Unclean (不整洁)', 'Unclear (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['Self-rated health'] = input_df['Self-rated health'].replace(['Very Good (非常好)', 'Good (很好)', 'Fair (好)', 'Average (一般)', 'Poor (不好)', 'Not Sure (不清楚)'], [1, 2, 3, 4, 5, -1])
    input_df['Smoke status'] = input_df['Smoke status'].replace(['Currently smoking (目前吸烟)', 'Quit smoking (已经戒烟)', 'Never smoke (从不吸烟)', 'Not Sure (不清楚)'], [1, 2, 3, -1])

    return input_df



# Define function to call
# 定义一个函数，实现导入模型，预测新数据，给出预测概率
def make_predict(input_df):
    # Load the trained model for predictions
    with open("sklearn_RF_best_model.sav", "rb") as f:
        model = pickle.load(f)

    # make prediction
    predict_result = model.predict(input_df)  # 对输入的数据进行预测

    # check probability
    predict_probability = model.predict_proba(input_df)  # 给出预测概率
    return predict_result, predict_probability


# # 设置一个按钮用于预测
# if st.button('Please click the button to predict（请点击进行预测）'):
#     # 检查是否完成了所有选项
#     if input_df.isnull().values.any():
#         st.warning("You have unfinished questions, please make sure you have completed all of them！\n您有问题未完成，请确保完成了所有选项！")
#     else:
#         # 在这里执行预测相关的代码

#         input_df1 = codeing_fun(input_df=input_df)
#         result, probability = make_predict(input_df=input_df1)

#         # 显示结果
#         st.header('Your cancer risk level:\n您的癌症风险等级：')

#         if int(result) == 1:
#             st.write("You may belong to a high-risk group.\n您可能属于高危人群")
#             # st.write(f"概率：{probability}")
#         else:
#             st.write("You may belong to a low-risk group.\n您可能属于低危人群")
#             # st.write(f"概率：{1 - probability}")
# 存储未完成的问题的索引

# 设置一个按钮用于预测
if st.button('Please click the button to predict（请点击进行预测）'):
    # 检查是否完成了所有选项
    if input_df.isnull().values.any():
        st.warning("You have unfinished questions, please make sure you have completed all of them！\n您有问题未完成，请确保完成了所有选项！")
        
        # 记录未完成的问题的索引
        unfinished_questions = [index for index, row in input_df.iterrows() if row.isnull().any()]
        
        # 自动跳转到第一个未完成的问题
        if unfinished_questions:
            first_unfinished_index = unfinished_questions[0]
            
            # 获取问题所在的位置
            question_element_id = f"question_{first_unfinished_index}"
            
            # 使用 JavaScript 代码获取问题元素的垂直位置
            js_code = f"""
            <script>
                var questionElement = document.getElementById('{question_element_id}');
                var questionPosition = questionElement.offsetTop;
                window.parent.postMessage({{scrollTo: questionPosition}}, "*");
            </script>
            """
            
            # 在 Streamlit 中执行 JavaScript 代码
            st.components.v1.html(js_code, height=0)
    else:
        # 在这里执行预测相关的代码
        input_df1 = codeing_fun(input_df=input_df)
        result, probability = make_predict(input_df=input_df1)

        # 显示结果
        st.header('Your cancer risk level:\n您的癌症风险等级：')

        if int(result) == 1:
            st.write("You may belong to a high-risk group.\n您可能属于高危人群")
            # st.write(f"概率：{probability}")
        else:
            st.write("You may belong to a low-risk group.\n您可能属于低危人群")
            # st.write(f"概率：{1 - probability}")

# 为每个问题添加唯一的标识符
for index, row in input_df.iterrows():
    question_element_id = f"question_{index}"
    st.write(f'<div id="{question_element_id}">{row.name}</div>', unsafe_allow_html=True)

