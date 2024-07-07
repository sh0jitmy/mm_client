import ollama

#multi modal 
res = ollama.chat(
	model="llava-llama3",
	messages=[
		{
			'role': 'user',
			'content': 'Describe this image:',
			'images': ['./test.png']
		}
	]
)
print(res['message']['content'])
mm_out = res['message']['content']

#mm_out = "The image presents a detailed view of a waveform, captured in the digital audio workspace (DAW) software. The waveform is represented as a series of yellow lines against a black background. It appears to be an audio track, with small peaks and valleys indicating the amplitude variations of the signal over time. In the top left corner of the image, there's a toolbar, colored in gray, which provides various tools for editing and manipulating the waveform. The bottom right corner features a frequency spectrum, also rendered in yellow lines on a black background. This spectrum gives a visual representation of the frequency components present in the audio track.The software interface is labeled with different buttons, each serving a unique purpose in the process of audio production or post-production. However, the exact labels are not discernible from the image. The overall layout and design of the software suggest a professional-grade tool used by audio engineers for precise control over their work. Please note that this description is based on the visible elements in the image and does not include any speculative or imaginary content." 


# Translate Japanese
contents = "以降の文を翻訳して\n" + mm_out
res = ollama.chat(
	model="elyza:jp8b",
	messages=[
		{
			'role': 'user',
			'content': contents,
		}
	]
)
print(res['message']['content'])
