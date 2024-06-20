import gradio as gr
from qrMod import qr

demo = gr.Interface(fn=qr, inputs='text', outputs=gr.Image())
demo.launch(share=True)