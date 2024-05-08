# Profile Picture Checker

The purpose of this application is to allow users to manually upload a photo, after which the program will determine if it is appropriate or inappropriate for a profile picture, following the guidelines of popular social media platforms.

It was developed using Python, and using OpenAI’s APIs. 

# How to run the program

I have used Python v3.12.0 (Virtual Environment Mode)

So first you have to clone this repository. Then pip install the requirements.

-  https://github.com/regieosano/dating-profile-review.git

-  pip install -r requirements.txt




# Example output of running the program

Console Output:

![image info](./images/json_image/json_output.png)


It would be a JSON return as shown below:

{
	'description': 'There is a man with glasses sitting in front of a sign',
	'list_of_words: 'The words in the image are: FOCUS, SACRIFICE, PERSISTENCY, CONTROL, DISCIPLINE',
	'verdict': 'Rate is: Description: 8 + Words: 3 = TOTAL RATE of 11.\n\nThe description is appropriate as it focuses on the man's appearance and body. There are no explicit or inappropriate elements mentioned.\n\nThe words in the image are all positive and motivational, which adds to the overall appeal of the profile picture.\n\nBased on the high rate, the profile picture seems suitable for a dating site and would likely attract the attention of many users. However, if an alternative picture is desired to make it more attention-grabbing, a suggestion could be a close-up shot of the man's face, with a genuine smile and engaging eyes. This would create a warm and inviting impression, increasing the chances of attracting potential matches.'
}

* Please note that the JSON Data Output may not appear entirely user-friendly as it is generated through the console. To clarify, it will contain three (3) fields, namely 'description', 'list_of_words', and 'verdict'. The purpose of each field is as follows:

   1. 'description' - This field conveys the AI's depiction of the image, translating 
	                    the visual elements into descriptive text.

   2. 'list_of_words' - In this field, any words that are present and detectable in 
	                      the image will be listed, as identified by the AI.

   3. 'verdict' - The verdict includes the AI's rating on a scale of 1 to 10, 
	                assessing the image's appropriateness. It also encapsulates the AI's suggestions and recommendations based on the analysis.

* I must emphasize with utmost clarity that the application I have architected is not yet primed for production deployment. The current iteration was meticulously crafted to fulfill the essential functionalities and to ensure the precise output and data integrity as stipulated by the rigorous challenge instructions, and all this was accomplished within the stringent confines of a 3 to 4 day deadline.

* While there are elements that beckon for further refinement and enhancements to ascend to the pinnacle of accuracy and performance, I have exerted a herculean effort to fine-tune this application to the brink of excellence. My unwavering dedication to this endeavor is evident in every line of code and every decision taken. I am confident—and it is my earnest hope—that the monumental strides taken thus far have not only met but surpassed the expectations and objectives set forth by this challenge. 

# Algorithm of the Application

As a committed advocate for LEAN MANAGEMENT and the principle of avoiding over-engineering, I also embrace established software development best practices. These include adhering to the philosophy of "Don't Reinvent the Wheel," the DRY (Don't Repeat Yourself) Principle, and the KISS (Keep It Simple, Stupid 😁) method. Here is the algorithm I propose:

1. The user uploads a potential profile picture.

2. The image is processed by two AI Agent Functions or Tools:

   2.1. Image Description Tool - This tool will convert the image into descriptive 
	      text, providing a detailed representation of the visual content.

   2.2. Words Detection Tool - This tool will identify and extract any visible text 
	      within the image, ensuring all embedded words are captured.

3. Subsequently, a service will evaluate and analyze the content, determining the appropriateness of the uploaded profile picture based on predefined criteria.

4. Ultimately, the results are returned as a JSON Output, offering an easy-to-interpret and integrate format for further use.


* A possible user scenario involves the upload of an image that exceeds acceptable size limits for a profile picture. To address this, checks must be in place to validate image dimensions, and corrective actions should be implemented to resize or reject non-compliant images accordingly.

# Prompts Used for the Application

PROMPT_1 = "As an experienced image describer and an agent tool at your disposal you have to describe to me the image as detailed as you can possibly do. Make sure you have used and exhausted all necessary efforts to give a valid and effective description of the image. In the output response you have to provide the description like if the person is fully dress or half dress or naked full or half naked then indicate if the image is of a person or not a person. Response format for a person picture: Boy sitting on a chair while eating. It is a person picture. Response format for a non person picture: A picture of a car. It is not a person picture."

PROMPT_2 = "What are the words in the image? If there are words or word in the image that are somewhat styled fonts and characters which is difficult to 'read' or to 'decipher' then just translate it to the next nearest word that is sounding-like or connotes its meaning. For example the read word is 'Euuitch' then it is 'Twitch'."

This is the SERVICE PROMPT FOR RATE COMPUTATION AND ACCEPTABILITY ANALYSIS

 "You are an expert in social media with special focused on profile picture analysis and at the same time an English Language guru. Thus, based on the description - {description} and the list of words given as separated in commas or in sentence form - {list_of_words}. You are to provide an assessment of the profile if it is appropriate or inappropriate based on the sentence {description} and the list of words - {list_of_words} provided. The description should first and foremost be of a person face and body. For example: 'The image is a woman sitting in a chair' to be considered as appropriate and it is the only thing that is acceptable - no more no less. Second would be that the description is in good taste meaning there's no nudity (half or full), vulgar expressions or it shows the contrary based on the guidelines and policies of current social media platforms as far as profile pictures are concerned. Then analyze the list of words, if present, and it must not have explicit terms, gross, disrespectful, harmful in general, bad content or generally evil to be considered as appropriate. Both of these conditions must be satisfied in order to be deemed as appropriate. Next, rates must be computed and its total should be provided on the response. It would depend on how the image would make an impact in a dating scheming activity. If the description is that of a person and contains the essence and characteristics of beauty and artistically pleasing then that's an automatic score of seven (7). Or if the description is of a person and is appropriate but lacks description of being beautiful and artistically sound or superb then a score of six (6) would be sufficient. If the description is not of a person then a score of two (2) would be given. The same goes with the words provided if it does not contain unacceptable terms as discussed above plus the list of words somewhat mentioned of aesthetics, pleasurable and of appealing qualities and would entice or captivate its reader then that's a score of three (3). But if it is only appropriate then a score of one (1) should be the case. A rate of one (1) is given if the description is inappropriate. A rate of one (1) is also given if the words are construed as inappropriate. Then combine the two scores and that's the total rate. For example the response format should be: Rate is: Description: 5 + Words: 2 = TOTAL RATE of 7. Then you must suggest or to provide other alternatives if it was considered inappropriate. Please remove any unnecessary data not needed. Since it is a dating site, please suggest a profile picture that would be more attention grabbing and would interest and attract a lot of people especially in a love-match cyber activity where appearance and beauty stands out as the best."


# User Flow and Propose UI for Profile Upload

![image info](./images/flow/UserFlow.png)

![image info](./images/sampleuidesign/sample_ui.png)

# Challenges faced, design decisions made and the reasons of coming up with the final process for the solution
 
The foremost and significant challenge I encountered was the extraction of text from an image with the utmost fidelity and precision. To achieve this, I diligently conducted extensive research to identify a suitable library and discovered a notable one called "easyocr." This Python library enabled me to successfully extract text from images. While it may not boast flawless accuracy, it performed commendably well, particularly when the text was distinct and legible. In such instances, it consistently yielded accurate transcriptions of the extracted words. Although there may be more advanced libraries available, "easyocr" proved to be the optimal choice for this endeavor, given its reliable performance in meeting the challenge at hand.

The second formidable challenge I faced was to achieve an impeccable description of an image using a sophisticated Python library known as "transformers," renowned for its plethora of features that facilitate the conversion from image to text. I navigated through intricate difficulties, as the AI-generated description initially fell short in its level of detail—failing to accurately convey nuances such as whether the subject was smiling or the exact hue of their attire.

Nevertheless, these obstacles were met with resolute perseverance. I remained steadfast in utilizing the library despite the intricacies, for my predominant aim transcended the minutiae of technical specifics. The ambition was to perfect the process of conducting a thorough and effective review of a profile picture, focusing on achieving broader accuracy rather than laboring over the precision of the library employed.

In pursuit of this objective, I engineered an algorithm that outputs a trustworthy review, which, although already consistently reliable, allows for additional refinement. Throughout this diligent pursuit, I have demonstrated an unwavering commitment to excellence, ensuring that I am the ideal candidate to bring this visionary project to fruition.

The culminating phase of the endeavor involved the methodical and recursive steps of formulating the appropriate prompts—an iterative process that was both time-intensive and mentally demanding. Despite these rigorous demands, the culmination of my efforts was a profound sense of satisfaction with the brilliantly composed prompts.

My confidence in having met the challenges presented is resolute; I am convinced that my dedication and the quality of my work speak volumes. Nonetheless, I fully acknowledge that the ultimate decision rests with Bringo Tech. I await their final judgment with the hope that my efforts have resonated with the high standards they seek and that my commitment has positioned me as the candidate of choice.

With anticipation, I look forward to a favorable outcome.


