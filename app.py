import streamlit as st
# Eda packages

import pandas as pd
import numpy as np

#Data viz packages

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

#function

def main():
    
    title_container1 = st.container()
    col1, col2 ,  = st.columns([6,12])
    from PIL import Image
    image = Image.open('static/asia.jpeg')
    with title_container1:
        with col1:
            st.image(image, width=200)
        with col2:
            st.markdown('<h1 style="color: tomato;">ASIA Consulting</h1>',
                           unsafe_allow_html=True)
    
    st.subheader('Body Mass Index')
    
    
    
    
    st.sidebar.image("static/rhe.jpg", use_column_width=True)
    activites = ["About","BMI calculator","BMI finding by file"]
    choice =st.sidebar.selectbox("Select Activity",activites)
 
    if choice == 'About':
        st.subheader("About BMI")
        title_container1 = st.container()
        col1, col2 ,  = st.columns([4,20])
        from PIL import Image
        image = Image.open('static/Logo.jpg')
        with title_container1:
            
            with col2:
                st.image(image, width=400, caption='BMI')
            
        st.markdown("""**❓ What is BMI?**
                    
The Body Mass Index (BMI) Calculator can be used to calculate BMI value and corresponding weight status while taking age into consideration. """)
        
        title_container1 = st.container()
        col1, col2 ,  = st.columns([12,12])
        from PIL import Image
        image = Image.open('static/rheu.png')
        with title_container1:
            with col1:
                st.image(image, width=350, caption='BMI meter')
                
            with col2:
                st.image("https://thumbs.gfycat.com/BriskEnviousGrizzlybear-size_restricted.gif", width=385, caption='Impacts of BMI')

        
        
        st.markdown("""**❓ BMI introduction**

BMI is a measurement of a person's leanness or corpulence based on their height and weight, and is intended to quantify tissue mass. It is widely used as a general indicator of whether a person has a healthy body weight for their height. Specifically, the value obtained from the calculation of BMI is used to categorize whether a person is underweight, normal weight, overweight, or obese depending on what range the value falls between. These ranges of BMI vary based on factors such as region and age, and are sometimes further divided into subcategories such as severely underweight or very severely obese. Being overweight or underweight can have significant health effects, so while BMI is an imperfect measure of healthy body weight, it is a useful indicator of whether any additional testing or action is required. Refer to the table below to see the different categories based on BMI that are used by the calculator.
""")
        st.markdown("""**➡️➡️ BMI table for adults**

This is the World Health Organization's (WHO) recommended body weight based on BMI values for adults. It is used for both men and women, age 18 or older.                   
        """)
        title_container1 = st.container()
        col1, col2 ,  = st.columns([4,15])
        from PIL import Image
        image = Image.open('static/table.jpg')
        with title_container1:
            
            with col2:
                st.image(image, width=450, caption='BMI Table')
        
        st.markdown("""**🕮🕮  Risks associated with being overweight**
                    
Being overweight increases the risk of a number of serious diseases and health conditions. Below is a list of said risks, according to the Centers for Disease Control and Prevention (CDC):

- High blood pressure
- Higher levels of LDL cholesterol, which is widely considered "bad cholesterol," lower levels of HDL cholesterol, considered to be good cholesterol in moderation, and high levels of triglycerides
- Type II diabetes
- Coronary heart disease
- Stroke
- Gallbladder disease
- Osteoarthritis, a type of joint disease caused by breakdown of joint cartilage
- Sleep apnea and breathing problems
- Certain cancers (endometrial, breast, colon, kidney, gallbladder, liver)
- Low quality of life
- Mental illnesses such as clinical depression, anxiety, and others
- Body pains and difficulty with certain physical functions
- Generally, an increased risk of mortality compared to those with a healthy BMI
- As can be seen from the list above, there are numerous negative, in some cases fatal, outcomes that may result from being overweight. Generally, a person should try to maintain a BMI below 25 kg/m2, but ideally should consult their doctor to determine whether or not they need to make any changes to their lifestyle in order to be healthier.                   
                    

                    """)
                    
        st.markdown("""**🕮🕮  Risks associated with being underweight**
                    
Being underweight has its own associated risks, listed below:

- Malnutrition, vitamin deficiencies, anemia (lowered ability to carry blood vessels)
- Osteoporosis, a disease that causes bone weakness, increasing the risk of breaking a bone
- A decrease in immune function
- Growth and development issues, particularly in children and teenagers
- Possible reproductive issues for women due to hormonal imbalances that can disrupt the menstrual cycle. Underweight women also have a higher chance of miscarriage in the first trimester
- Potential complications as a result of surgery
- Generally, an increased risk of mortality compared to those with a healthy BMI
- In some cases, being underweight can be a sign of some underlying condition or disease such as anorexia nervosa, which has its own risks. Consult your doctor if you think you or someone you know is underweight, particularly if the reason for being underweight does not seem obvious.                  
                    

                    """)
        st.markdown("""**🕮🕮  Limitations of BMI**
                    
Although BMI is a widely used and useful indicator of healthy body weight, it does have its limitations. BMI is only an estimate that cannot take body composition into account. Due to a wide variety of body types as well as distribution of muscle, bone mass, and fat, BMI should be considered along with other measurements rather than being used as the sole method for determining a person's healthy body weight.                  
                    

                    """)
        st.markdown("""**- In adults:**
                    
BMI cannot be fully accurate because it is a measure of excess body weight, rather than excess body fat. BMI is further influenced by factors such as age, sex, ethnicity, muscle mass, and body fat, and activity level, among others. For example, an older person who is considered a healthy weight, but is completely inactive in their daily life may have significant amounts of excess body fat even though they are not heavy. This would be considered unhealthy, while a younger person with higher muscle composition of the same BMI would be considered healthy. In athletes, particularly bodybuilders who would be considered overweight due to muscle being heavier than fat, it is entirely possible that they are actually at a healthy weight for their body composition. Generally, according to the CDC:

- Older adults tend to have more body fat than younger adults with the same BMI.
- Women tend to have more body fat than men for an equivalent BMI.
- Muscular individuals and highly trained athletes may have higher BMIs due to large muscle mass.
                    """)
        st.markdown("""**- In children and adolescents:**
                    
The same factors that limit the efficacy of BMI for adults can also apply to children and adolescents. Additionally, height and level of sexual maturation can influence BMI and body fat among children. BMI is a better indicator of excess body fat for obese children than it is for overweight children, whose BMI could be a result of increased levels of either fat or fat-free mass (all body components except for fat, which includes water, organs, muscle, etc.). In thin children, the difference in BMI can also be due to fat-free mass.

That being said, BMI is fairly indicative of body fat for 90-95% of the population, and can effectively be used along with other measures to help determine an individual's healthy body weight.      """)
        
        st.markdown("""**❓ BMI formula**
                    
Below are the equations used for calculating BMI in the International System of Units (SI) and the US customary system (USC)
       """)
       
        title_container1 = st.container()
        col1, col2 ,  = st.columns([4,15])
        from PIL import Image
        image = Image.open('static/formula.jpg')
        with title_container1:
            
            with col2:
                st.image(image, width=450, caption='Formula to find BMI')
        

    elif choice == 'BMI calculator':
        
        st.subheader(" 🔍 Lets find BMI")
        
        name=st.text_input("Enter your name")
        gender=st.radio("What is your gender",("Male","Female"))
        selection=st.selectbox("Select your age group",["10-17","18-34","35-44","45-54","55-64","65-74","75-79"])
        height=st.slider("Your height(in cm)",1,500)
        weight=st.slider("Your weight(in kilograms)",5,300)
        bmi=(weight/(height*height)*10000)
        bmi=round(bmi, 2)
        
        
       
        
        if bmi==0.11:
                st.text("      ")
        if st.button("Submit"):
            st.subheader("🔍 Results")
        	
            st.write('**✨ Hi {0} your BMI is {1} Kg/m2**'.format(name,bmi))
            
            if bmi < 18.5:
                st.warning("**You are Underweight!!**") 
                st.write("**💡Here are some healthy ways to gain weight when you're underweight:**")
	           
                st.info("""1. Eat more frequently. 
                        
When you're underweight, you may feel full faster. Eat five to six smaller meals during the day rather than two or three large meals.""")
                st.info("""2. Choose nutrient-rich foods. 
                        
As part of an overall healthy diet, choose whole-grain breads, pastas and cereals; fruits and vegetables; dairy products; lean protein sources; and nuts and seeds.""")
                st.info("""3. Try smoothies and shakes. 
Don't fill up on diet soda, coffee and other drinks with few calories and little nutritional value. Instead, drink smoothies or healthy shakes made with milk and fresh or frozen fruit, and sprinkle in some ground flaxseed. In some cases, a liquid meal replacement may be recommended.""")
                st.info("""4. Watch when you drink. 
Some people find that drinking fluids before meals blunts their appetite. In that case, it may be better to sip higher calorie beverages along with a meal or snack. For others, drinking 30 minutes after a meal, not with it, may work.""")
                st.info("""5. Make every bite count. 
Snack on nuts, peanut butter, cheese, dried fruits and avocados. Have a bedtime snack, such as a peanut butter and jelly sandwich, or a wrap sandwich with avocado, sliced vegetables, and lean meat or cheese.""")
                st.info("""6. Top it off. 
Add extras to your dishes for more calories — such as cheese in casseroles and scrambled eggs, and fat-free dried milk in soups and stews.""")
                st.info("""7. Have an occasional treat.
Even when you're underweight, be mindful of excess sugar and fat. An occasional slice of pie with ice cream is OK. But most treats should be healthy and provide nutrients in addition to calories. Bran muffins, yogurt and granola bars are good choices.""")
                st.info("""8. Exercise. 
Exercise,especially strength training, can help you gain weight by building up your muscles. Exercise may also stimulate your appetite.""")   
                
            if bmi >= 18.5 and bmi<= 24.9:
                st.warning("**🥳 You are under Normal Range!!**") 
                st.write("**💡Here are some healthy ways to keep maintaining your Normal Range BMI**")
	           
                st.info("""1.Diet
                        
Tips for maintaining a healthy (normal) BMI
For starters, if you've not been eating healthy lately, you'll have to make rather dramatic changes in your diet plan.
A balanced and nutritious diet goes a long way in helping you achieve a healthy body weight (thus, a normal BMI).
Include more veggies and whole foods in your diet.
And, let go of oily, fatty, and junk food.""")

                st.info("""2. Exercise
                        
Exercise regularly and religiously!
The toughest part about starting to exercise is the starting part itself- once you get going, it only becomes easier.
So, make exercise a regular and religious part of your life, to score a healthier BMI score.
Not only will exercise get you in a better shape, it will also improve your overall mental and physical well-being.""")
                st.info("""3. Rest
                        
Proper rest is important for maintaining a healthy weight
Getting proper rest is just as important as eating the right food items and exercising regularly, if not more, in order to maintain a healthy weight.
Assure yourself a regular sound sleep of at least 7-8 hours to let your body recover from the workout.
Also, build a consistent daily sleep schedule.
Not just that, consider reducing your screen-time as it promotes sedentary habits.""")

            if bmi >= 25.0 and bmi<= 29.9:
                st.warning("**You are Overweight!!**") 
                st.write("**💡Here are some healthy ways to control your overweight**")
	           
                st.info("""1. Include Highly Nutritious Foods in Your Diet
                        
Many people think that losing weight means you have to stop eating food. This is far from the truth. As a matter of fact, while you are on a weight loss regime, it is vital that you consume nutrition-rich food over junk food.
This means you have to pick a diet that helps you maintain your energy without weight. You can opt for fresh fruits, fish, legumes, nuts, whole grains, brown rice, etc. Minimise the consumption of oily food, processed meats, baked goods, white bread, processed food, etc. Also, make changes to your lifestyle habits such as avoiding drinking and smoking as it can pose a risk to your health in the long run.
If you are finding it challenging to decide on a diet for yourself, get in touch with a dietician to help you plan a meal.""")

                st.info("""2. Keep Track of Your Food and Weight
                        
It is necessary that you keep records of your weight loss regime. There are various mobile apps and websites that allow tracking of each food item you consume over the day and calculate your total calories intake. It also helps you measure your progress by tracking your weight on a weekly basis and making the necessary changes and adjustments to diet and exercise over time.""")
                st.info("""3. Exercise Regularly
While you maintain a nutrition-rich diet, you also have to get into the habit of working out regularly. A good exercise routine will help you both physically and mentally in the long run. Dedicate a few good minutes/hours of your day to work out. You can choose exercises that can be done at home or go to a gym.

On the other hand, you can turn your daily activities into fitness goals, such as:

 

- Taking stairs instead of the lift

- Walking your dog

- Gardening

- Dancing

- Playing more outdoor games""")
                st.info("""Note: 
People who are severely obese or have heart-related health risks need to consult their doctors before taking up any intensive workout sessions. It is also a good idea to consult a professional dietician before making any drastic changes to your diet.""")
                
            if bmi >= 30 :
                st.warning("**You are under Obesity!!**") 
                st.write("**💡Here are some healthy ways to control your obesity**")
	           
                st.info("""1. Changing your habits
                        
Changing your eating and physical activity habits and lifestyle is difficult, but with a plan, effort, regular support, and patience, you may be able to lose weight and improve your health. The following tips may help you think about ways to lose weight, engage in regular physical activity, and improve health over the long-term.

- Be prepared for setbacks—they are normal. 
After a setback, like overeating at a family or workplace gathering, try to regroup and focus on getting back to your healthy eating plan as soon as you can. Try to eat only when you’re sitting at your dining room or kitchen table. At work, avoid areas where treats may be available. Track your progress using online food or physical activity trackers, such as the Body Weight Planner, that can help you keep track of the foods you eat, your physical activity, and your weight. These tools may help you stick with it and stay motivated.
- Set goals. 

Having specific goals can help you stay on track. Rather than “be more active,” set a goal to walk 15 to 30 minutes before work or at lunch on Monday and Friday. If you miss a walk on Monday, pick it up again Tuesday.
- Seek support. 
Ask for help or encouragement from your family, friends, or health care professionals. You can get support in person, through email or texting, or by talking on the phone. You can also join a support group. Specially trained health professionals can help you change your lifestyle.""")

                st.info("""2. Weight-management programs
Some people benefit from a formal weight-management program. In a weight-management program, trained weight-management specialists will design a broad plan just for you and help you carry out your plan. Plans include a lower-calorie diet, increased physical activity, and ways to help you change your habits and stick with them. You may work with the specialists on-site (that is, face-to-face) in individual or group sessions. The specialists may contact you regularly by telephone or internet to help support your plan. Devices such as smartphones, pedometers, and accelerometers may help you track how well you are sticking with your plan.

Some people may also benefit from online weight-management programs or commercial weight-loss programs.""")
                st.info("""3. Weight-loss medicines
When healthy eating and physical activity habits are not enough, your doctor may prescribe medicines to treat overweight and obesity.

You should try to stick with your healthy eating plan and continue getting regular physical activity while taking weight-loss medicines.

You may see ads for herbal remedies and dietary supplements NIH external link that claim to help you lose weight. But many of these claims are not true. Some of these supplements can even have serious side effects. Talk with your doctor before taking any over-the-counter herbal remedies or dietary supplements for the purpose of trying to lose weight.""")
                st.info("""4. Weight-loss devices
Your doctor may consider weight-loss devices External link if you haven’t been able to lose weight or keep from gaining back any weight you lost with other treatments. Because weight-loss devices have only recently been approved, researchers do not have long-term data on their safety and effectiveness. Weight-loss devices include

- Electrical stimulation system. The electrical stimulation system uses a device a surgeon places in your abdomen with laparoscopic surgery NIH external link. The device blocks nerve activity between your stomach and brain.
- Gastric balloon system. For the gastric balloon system, a doctor places one or two balloons in your stomach through a tube that goes in your mouth. Once the balloons are in your stomach, the surgeon fills them with salt water so they take up more space in your stomach and help you feel fuller.
- Gastric emptying system. A gastric emptying system uses a pump to drain part of the food from your stomach after a meal. The device includes a tube that goes from the inside of your stomach to the outside of your abdomen. About 20 to 30 minutes after eating, you use the pump to drain the food from your stomach through the tube into the toilet. 
People who are severely obese or have heart-related health risks need to consult their doctors before taking up any intensive workout sessions. It is also a good idea to consult a professional dietician before making any drastic changes to your diet.""")
                st.info("""5. Bariatric surgery
Bariatric surgery includes several types of operations that help you lose weight by making changes to your digestive system. Bariatric surgery may be an option if you have extreme obesity and haven’t been able to lose enough weight to improve your health or keep from gaining back the weight you lost with other treatments. Bariatric surgery also may be an option at lower levels of obesity if you have serious health problems, such as type 2 diabetes or sleep apnea, related to obesity. Bariatric surgery can improve many of the medical conditions linked to obesity, especially type 2 diabetes.""")
                st.info("""6. Special diets
- Calorie-restricted diets
Your doctor may recommend a lower-calorie diet such as 1,200 to 1,500 calories a day for women and 1,500 to 1,800 calories a day for men. The calorie level depends on your body weight and physical activity level. A lower calorie diet with a variety of healthy foods will give you the nutrients you need to stay healthy.

- Intermittent fasting
Intermittent fasting is another way of reducing food intake that is gaining attention as a strategy for weight loss and health benefits. Alternate-day fasting is one type of intermittent fasting that consists of a “fast day” (eating no calories to one-fourth of caloric needs) alternating with a “fed day,” or a day of unrestricted eating. Researchers have conducted only a few studies of intermittent fasting as a strategy for weight loss. They have no long-term data on the safety and effectiveness of intermittent fasting for long-term weight maintenance.""")
        
        
    elif choice == 'BMI finding by file':
        
        form=pd.read_excel('static/temp.xlsx')
        import base64
        import io
        towrite = io.BytesIO()
        downloaded_file = form.to_excel(towrite, encoding='utf-8', index=False, header=True) # write to BytesIO buffer
        towrite.seek(0)  # reset pointer
        b64 = base64.b64encode(towrite.read()).decode() 
        linko= f"<p style='font-family:sans-serif; color:Black; font-size: 20px;'> Your File must include these 2 columns as in Template file <a href='data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}' download='bmi_template.xlsx' >Download Template </a> </p> "
        st.markdown(linko, unsafe_allow_html=True)
        st.subheader(" Upload your file")
        @st.cache(allow_output_mutation=True)
        def get_df(file):
          # get extension and read file
          extension = file.name.split('.')[1]
          if extension.upper() == 'CSV':
            df = pd.read_csv(file)
          elif extension.upper() == 'XLSX':
            df = pd.read_excel(file)
          
          return df
        file = st.file_uploader("Upload file", type=['csv' 
                                                 ,'xlsx'])
        if not file:
            st.write("Upload a .csv or .xlsx file to get started")
            return
          
        df = get_df(file)
        if st.checkbox("Lets find all the Related feature for BMI"):
            df['BMI']=df['weight(kg)']/(df['height(m)']*df['height(m)'])
            df['BMI']=round(df['BMI'], 2)
            
            from scipy.stats import zscore

            df[['BMI_zscore','age_zscore','weight(kg)_zscore','height(m)_zscore']]=df[['BMI','age','weight(kg)','height(m)']].apply(zscore) 
        
            def determine_bmi(BMI):
                if BMI < 18.5:
                    return 'Underweight'
                elif BMI >= 18.5 and BMI<= 24.9:
                    return 'Normal'
                elif BMI >= 25.0 and BMI<= 29.9:
                    return 'Overweight'
                elif BMI >= 30:
                    return 'Obesity'
                        
            df["category"] = df["BMI"].apply(lambda x: determine_bmi(x))
        
            st.write(df.head())
            
            st.text("Download the Above Data table by clicking on Download CSV")
            st.download_button(label='Download CSV',data=df.to_csv(),mime='text/csv')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
              
            
    st.text('© ASIA Consulting 2022') 
            




if __name__=='__main__':
    main()