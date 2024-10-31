import requests
import streamlit as st

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "90724770-9749-11ef-a556-d368dce4f7aeab04782e-2a74-4e1c-acff-0ef1c4b0efbc"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to something you want your machine learning model to classify

# while True :
question = st.text_input ("호텔에 대해 궁금하신 사항을 입력해주세요", key = "<uniquevalueofsomesort>")

if question != "":

    # if (question == "나가기"):
    #     break

    demo = classify(question)

    label = demo["class_name"]
    confidence = demo["confidence"]

    if confidence < 50:
        st.write ("질문을 이해하지 못했어요. 다시 질문해주시겠습니까?")
    elif label == "location":
        st.write ("호텔은 도심에 위치해 있어 주요 관광명소와의 접근성이 매우 좋습니다.")
    elif label == "service":
        st.write ("저희 호텔은 24시간 프런트 데스크와 룸서비스를 제공하여 편리한 서비스를 보장합니다.")
    elif label == "price":
        st.write ("1박 요금은 10만 원부터 시작하며, 시즌에 따라 변동이 있을 수 있습니다.")
    elif label == "checkinout":
        st.write ("체크인은 오후 3시부터 가능하며, 체크아웃은 오전 11시까지입니다.")
    elif label == "facility":
        st.write ("실내 수영장, 헬스장, 스파 등 다양한 시설을 갖추고 있습니다.")
    elif label == "reservation":
        st.write ("예약은 웹사이트나 전화로 간편하게 하실 수 있으며, 취소 정책을 꼭 확인해 주세요.")

    # CHANGE THIS to do something different with the result
    st.write ("result: '%s' with %d%% confidence" % (label, confidence))

else :
    st.write ("데이터를 입력해주세요")
