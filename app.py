import streamlit as st

st.title("Title -> GeeksForGeeks")                       # Title
st.header("Header -> GeeksForGesks")                     # Header
st.subheader("Subheader -> GeeksForGesks")               # SubHeader
st.text("Text -> GeeksForGesks")                         # SubHeader

st.markdown('# Hi')                                      # Markdown
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')

st.success('Success')                                   # Success
st.info('Information')                                  # Info
st.warning('Information')                               # Warning
st.error('Information')                                 # Error
st.exception(ZeroDivisionError("Div not possible"))     # Exception

st.help(ZeroDivisionError)                              # Help   

st.write("range(1,10)")                                 # Write
st.write(range(1,10))
st.write(1*2*3)

st.code(                                                # Code
    'x = 10\n'
    'for i in range(x):\n'
    '\tprint(i)'
)

st.checkbox('Male')                                    # Checkbox

if(st.checkbox('Adult')):                              # Checkbox with validation
    st.write("You're an adult!")
                                                       # Radio Button
radioButton = st.radio('Select :', ('Male','Female','Other'))        
if(radioButton == 'Male'):
    st.write("Your're Male")
elif(radioButton == 'Male'):
    st.write("Your're Female")
elif(radioButton == 'Male'):
    st.write("Your're Other Gender")
                                                     
st.subheader("Select:")                               # SelectBox
selectbox = st.selectbox('Data Science: ', ['Data Analysis','Web Scraping','Machine Learning','Deep Learning','Natural Language Processing','Computer Vision','Image Processing'])  
st.write("You've selected: ",selectbox)

st.subheader("Select:")                               # MultiSelectBox
multiSelectBox = st.multiselect('Data Science: ', ['Data Analysis','Web Scraping','Machine Learning','Deep Learning','Natural Language Processing','Computer Vision','Image Processing'])  
st.write("You've selected: ",len(multiSelectBox),'courses')

st.subheader('Button')                               # Button
if(st.button("Click me")):
    st.write("You've clicked the button")

st.subheader("Slider")                               # Slider
vol = st.slider("Select the volume: ",0,100,1)
st.write("Volume is: ",vol)

st.subheader("Text Input")                           # Text-Input
username = st.text_input("Name: ")
if(username):
    st.write("Hi, ",username)

password = st.text_input("Password: ",type="password")

st.subheader("Text Area")                           # Text-Area
textarea = st.text_area("Write about yourself:")
st.write(textarea)

st.subheader("Input Number")                        # Input-Number
st.number_input("Enter your age: ",18,100)

st.subheader("Input Date")                          # Input-Date
st.date_input("Date: ")

st.subheader("Input Time")                          # Input-Time
st.time_input("Time: ")