# 代码目的：基于streamlit包生成网页

# 导入包
import pandas as pd
import streamlit as st
import joblib
import pickle

# main function
# 设置网页名称
st.set_page_config(page_title='癌症风险评估工具')

# 设置网页标题
st.header('中老年人癌症风险评估网页工具')

# 设置副标题
st.subheader('欢迎使用本工具！请您输入以下信息进行预测：')

# 添加说明文本
# 长文本会出现滑动条
# st.text('您可使用本工具预测未来4年内发生2型糖尿病的可能性。')
# st.text('请注意，本预测结果仅供参考，实际结果需以医生检查结果为准。')

# 在侧边栏添加图片
# st.sidebar.image('https://cdn.freebiesupply.com/logos/thumbs/1x/nvidia-logo.png', width=200)

# st.title('请您输入以下信息：')

# 在侧边栏添加说明
st.sidebar.info(
    '您可使用本工具预测现在癌症的可能性。请注意，本预测结果仅供参考，实际结果需以医生检查结果为准。')

# Function for online predictions
# 在侧边栏输入预测因子
# 添加滑动条
# factor1 = st.sidebar.selectbox(
#       'Age',
#        ('<50', '50-64', '>=65')
#    )  # 显示列表选择框

# 填写预测变量
# 社会人口学
factor1 = st.radio('Residence Type(户口类型)', ['Agricultural Type(农业户口)', 'None-Agricultural Type(非农户口)', 'Unified Residence Type(统一居民户口)', 'Unclear(不清楚)'])
factor2 = st.radio('Education Level(教育水平)', ['Elementary school or below(小学及以下)', 'Junior high school graduate(初中毕业)', 'High school or vocational school graduate(高中或中专毕业)', 'College diploma graduate(大专毕业)', 'Bachelor's degree or above(本科及以上)', 'Not sure(不清楚)'], index = None)
factor3 = st.radio('Marital Status(婚姻状态)', ['Married(已婚)', 'Single(未婚)', 'Divorced or widowed(离异或丧偶)', 'Not sure(不清楚)'], index = None)
factor4 = st.radio('Gender(性别)', ['Male(男性)', 'Female(女性)'], index = None)
factor5 = st.slider('Age(请选择您的年龄)', 45, 120)
factor6 = st.slider('Night Sleep Druation(您晚上的睡眠时间)', 0, 24)
factor7 = st.radio('How many meals do you eat every day？(您每日吃几顿饭？)', ['Four or more(每天大于等于四顿)', '每天三顿', '每天两顿', '每天一顿', '不清楚'], index = None)
factor8 = st.radio('您一年内喝酒频率', ['每个月超过一次', '每月少于等于一次', '不喝', '不清楚'], index = None)
factor9 = st.radio('您是否左胸痛？', ['是', '否', '不清楚'], index = None)
factor10 = st.radio('您是否有高血压？', ['是', '否', '不清楚'], index = None)
factor11 = st.radio('您是否有血脂异常？', ['是', '否', '不清楚'], index = None)
factor12 = st.radio('您是否有糖尿病？', ['是', '否', '不清楚'], index = None)
factor13 = st.radio('您是否有慢性肺部疾病？', ['是', '否', '不清楚'], index = None)
factor14 = st.radio('您是否有肝脏疾病？', ['是', '否', '不清楚'], index = None)
factor15 = st.radio('您是否有心脏病？', ['是', '否', '不清楚'], index = None)
factor16 = st.radio('您是否有中风？', ['是', '否', '不清楚'], index = None)
factor17 = st.radio('您是否有肾脏疾病？', ['是', '否', '不清楚'], index = None)
factor18 = st.radio('您是否有胃部或消化系统疾病？', ['是', '否', '不清楚'], index = None)
factor19 = st.radio('您是否有情感及精神方面问题？', ['是', '否', '不清楚'], index = None)
factor20 = st.radio('您是否有与记忆相关疾病？', ['是', '否', '不清楚'], index = None)
factor21 = st.radio('您是否有关节炎或风湿？', ['是', '否', '不清楚'], index = None)
factor22 = st.radio('您是否有哮喘？', ['是', '否', '不清楚'], index = None)
factor23 = st.radio('您是否有经历过交通事故或重大意外伤害？', ['是', '否', '不清楚'], index = None)
factor24 = st.radio('您是否有确诊青光眼？', ['是', '否', '不清楚'], index = None)
factor25 = st.radio('您的听力如何？', ['非常好', '很好', '好', '一般', '不好', '不清楚'], index = None)
factor26 = st.radio('您是否牙齿已经掉光？', ['是', '否', '不清楚'], index = None)
factor27 = st.radio('您是否经常身体疼痛？', ['是', '否', '不清楚'], index = None)
factor28 = st.radio('您是否一年内体重变化超过10斤？', ['是', '否', '不清楚'], index = None)
factor29 = st.radio('您小时候的营养情况如何？', ['非常好', '很好', '好', '一般', '不好', '不清楚'], index = None)
factor30 = st.radio('您的生活水平如何？', ['非常好', '相对好', '一般', '相对差', '很差', '不清楚'], index = None)
factor31 = st.radio('您的工作单位是？', ['政府部门或事业单位', '非盈利结构和企业', '个体户农户居民户', '其他', '不清楚'], index = None)
factor32 = st.radio('您家里的洗澡设施是什么样的？', ['统一供热水', '家庭自装热水器', '没有洗澡设施', '不清楚'], index = None)
factor33 = st.radio('您家里的供暖设施是什么样的？', ['太阳能', '煤炭或者蜂窝煤', '管道天然气或煤气', '液化石油气', '电', '烧秸秆、柴火', '其他', '不清楚'], index = None)
factor34 = st.radio('您家里的室内整洁度如何？', ['非常整洁', '很整洁', '整洁', '一般', '不整洁', '不清楚'], index = None)
factor35 = st.radio('您对自己的健康评价如何？', ['极好', '很好', '好', '一般', '不好', '不清楚'], index = None)
factor36 = st.radio('您的吸烟状态是如何的？', ['目前吸烟', '已经戒烟', '从不吸烟', '不清楚'], index = None)

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
    input_df['bc001'] = input_df['bc001'].replace(['农业户口', '非农户口', '统一居民户口', '不清楚'], [1, 2, 3, -1])
    input_df['bd001'] = input_df['bd001'].replace(['小学及以下', '初中毕业', '高中或中专毕业', '大专毕业', '本科及以上', '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['be001'] = input_df['be001'].replace(['已婚', '未婚', '离异或丧偶', '不清楚'], [1, 2, 3, -1])
    input_df['rgender'] = input_df['rgender'].replace(['男性', '女性'], [1, 2])
    input_df['da058'] = input_df['da058'].replace(['每天大于等于四顿', '每天三顿', '每天两顿', '每天一顿', '不清楚'], [1, 3, 4, 5, -1])
    input_df['da067'] = input_df['da067'].replace(['每个月超过一次', '每月少于等于一次', '不喝', '不清楚'], [1, 2, 3, -1])
    input_df['da003'] = input_df['da003'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da007_1_'] = input_df['da007_1_'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da007_2_'] = input_df['da007_2_'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da007_3_'] = input_df['da007_3_'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da007_5_'] = input_df['da007_5_'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da007_6_'] = input_df['da007_6_'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da007_7_'] = input_df['da007_7_'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da007_8_'] = input_df['da007_8_'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da007_9_'] = input_df['da007_9_'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da007_10_'] = input_df['da007_10_'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da007_11_'] = input_df['da007_11_'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da007_12_'] = input_df['da007_12_'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da007_13_'] = input_df['da007_13_'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da007_14_'] = input_df['da007_14_'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da021'] = input_df['da021'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da037'] = input_df['da037'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da039'] = input_df['da039'].replace(['非常好', '很好', '好', '一般', '不好', '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['da040'] = input_df['da040'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da041'] = input_df['da041'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da047'] = input_df['da047'].replace(['是', '否', '不清楚'], [1, 2, -1])
    input_df['da048'] = input_df['da048'].replace(['非常好', '很好', '好', '一般', '不好', '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['g003'] = input_df['g003'].replace(['非常好', '相对好', '一般', '相对差', '很差', '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['fb002'] = input_df['fb002'].replace(['政府部门或事业单位', '非盈利结构和企业', '个体户农户居民户', '其他', '不清楚'], [1, 2, 3, 4, -1])
    input_df['i018'] = input_df['i018'].replace(['统一供热水', '家庭自装热水器', '没有洗澡设施', '不清楚'], [1, 2, 3, -1])
    input_df['i021'] = input_df['i021'].replace(['太阳能', '煤炭或者蜂窝煤', '管道天然气或煤气', '液化石油气', '电', '烧秸秆、柴火', '其他', '不清楚'], [1, 2, 3, 4, 5, 6, 7, -1])
    input_df['i025'] = input_df['i025'].replace(['非常整洁', '很整洁', '整洁', '一般', '不整洁', '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['Self-rated health'] = input_df['Self-rated health'].replace(['极好', '很好', '好', '一般', '不好', '不清楚'], [1, 2, 3, 4, 5, -1])
    input_df['Smoke status'] = input_df['Smoke status'].replace(['目前吸烟', '已经戒烟', '从不吸烟', '不清楚'], [1, 2, 3, -1])

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


# 设置一个按钮用于预测
if st.button('点击进行预测'):
    # 检查是否完成了所有选项
    if input_df.isnull().values.any():
        st.warning("您有问题未完成，请确保完成了所有选项！")
    else:
        # 在这里执行预测相关的代码

        input_df1 = codeing_fun(input_df=input_df)
        result, probability = make_predict(input_df=input_df1)

        # 显示结果
        st.header('您的癌症风险：')

        if int(result) == 1:
            st.write("您可能属于高危人群")
            # st.write(f"概率：{probability}")
        else:
            st.write("您可能属于低危人群")
            # st.write(f"概率：{1 - probability}")

