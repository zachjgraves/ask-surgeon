import streamlit as st
import openai
import os
from PIL import Image

openai.api_key = os.environ["OPENAI_API_KEY"]

# Surgeon dictionary
people = {
    "Dr. John Hunter (1728 – 1793)": "Hunter is famous for approaching surgical \
        procedures with the scientific method in mind. He believed that \
        observation was necessary during surgery in order to determine the \
        best course of action for each patient. In other words, each patient’s \
        needs are different and surgery must be amended accordingly.",
    "Dr. Dominique Larrey (1766 – 1842)": "Considered one of the founders of \
        military surgery, Dominique Larrey was a surgeon during the Napoleonic \
        era in France. Larrey joined the French navy in 1786 and eventually \
        became surgeon-in-chief to the entire French Navy. He served in over 60 battles.",
    "Dr. Joseph Lister (1826 – 1912)": "Lister introduced the concept of sterilization \
        to surgery. Back in the day, people thought that diseases and infections \
        were the result of bad air. Lister began sterilizing surgical tools and \
        wounds, which resulted in fewer infections during and after surgery.",
    "Dr. Mary Edwards Walker (1832–1919)" : "The first female surgeon in the \
        United States. Graduating from Syracuse Medical College in 1855, she \
        faced challenges in establishing her surgical practice due to societal \
        norms. However, she became the first female surgeon in the US Army in \
        1863 and received the Congressional Medal of Honor in 1865. Although \
        the honor was temporarily revoked, it was reinstated in 1977. Dr. \
        Walker's remarkable achievements continue to be recognized.",
    "Dr. Daniel Hale Williams (1856–1931)" : "Daniel Hale Williams was an \
        African-American surgeon who founded Provident Hospital in 1891. It \
        was the first non-segregated hospital in the United States. Provident \
        also had an associated nursing school for African Americans.",
    "Dr. Jennie Smillie Robertson (1878–1981)" : "The first recorded female \
        surgeon in Canada. Despite the lack of Canadian internships or \
        residencies for women, she completed her training in the United States \
        and became a prominent gynecologist. Dr. Robertson played a key role \
        in establishing the Women's College Hospital and the Federation of \
        Medical Women of Canada.",
    "Dr. John Heysham Gibbon (1903 – 1973)": "Gibbon’s techniques and innovations \
        revamped surgical procedures of the heart as we know them today. \
        Gibbon was the first person to perform open-heart surgery. He was also \
        the inventer of the heart-lung machine.",
    "Dr. Lars Leksell (1907 – 1986) ": "Leksell invented the first fully functioning \
        stereotactic apparatus for use in human neurosurgery. As a result he is \
        considered one of the preeminent innovators of modern neurosurgery.",
    "Dr. Jessie Gray (1910–1978) " : "The first registered female general \
        surgeon in Canada. Graduating from the University of Toronto in 1934, \
        she became a trailblazer in her field, serving as the chief of surgery \
        at Women's College Hospital and earning recognition as Canada's \
        'First Lady of Surgery'",
    "Dr. Alexa Irene Canady (1950-Present)" : "Retired American pediatric \
        neurosurgeon. She became the first black woman to specialize in neurosurgery \
        after completing her residency in 1981. Dr. Canady served as the chief of \
        neurosurgery at the Children's Hospital in Michigan and was known for her \
        patient-focused approach. She received several awards and was inducted \
        into the Michigan Women's Hall of Fame."
}

# Front End
image = Image.open('header.jpg')
st.image(image, caption='Photo by Artur Tumasjan on Unplash')
st.title("Ask a Surgeon")
st.caption("NOTE: for entertainment purposes only, not medical advice")


question = []
question = st.text_area("Insert a question")

name = st.selectbox("Choose a person:", list(people.keys()))
description = people[name]

st.write(name)
st.write(description)

if st.button("Submit"):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Imagine you are the famous surgeon, {}. Description: {} \
        Answer this question in two paragraphs: {}?".format(name, description, question),
        max_tokens=1000,
        temperature=0.3,
        stream=True
    )

    with st.empty():
        collected_events = []
        completion_text = ''
        for event in response:
            collected_events.append(event)
            event_text = event['choices'][0]['text']
            completion_text += event_text
            st.write(completion_text)