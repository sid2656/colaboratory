import cv2
import os

import modules.scripts as scripts
import gradio as gr

def video2frame(video_path,output_folder):
    # 读取视频文件
    # video_path = 'path/to/video.mp4'
    cap = cv2.VideoCapture(video_path)

    # 检查视频是否成功打开
    if not cap.isOpened():
        print("Error opening video file")

    # 创建输出文件夹
    # output_folder = 'path/to/output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 逐帧读取视频并保存到输出文件夹
    frame_count = 1
    while cap.isOpened():
        # 读取一帧
        ret, frame = cap.read()

        # 检查是否成功读取帧
        if not ret:
            break

        # 指定输出文件名
        output_file = os.path.join(output_folder, f'{frame_count:04d}.png')
        print('\r geneframe:',output_file,end='')

        # 保存帧到输出文件
        cv2.imwrite(output_file, frame)

        # 更新帧计数器
        frame_count += 1

    # 释放视频对象
    cap.release()
    print('\n :) done!')

def frame2video(image_folder,ouput_dir,fps):
    # 读取图像文件列表
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.png') or f.endswith('.jpg')]
    image_files.sort()

    # 获取图像的宽度和高度
    img = cv2.imread(os.path.join(image_folder, image_files[0]))
    height, width, _ = img.shape

    # 创建输出视频对象
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(ouput_dir+'\output.mp4', fourcc, fps, (width, height))
    num_images = len(image_files)
    frame_num = 0
    # 逐帧写入视频帧
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        frame = cv2.imread(image_path)
        out.write(frame)
        frame_num +=1
        print('\r generating video:',f'{100*frame_num/num_images:5.2f}%',end='')

    # 释放视频对象
    out.release()
    print('\n :) done!')
    

class Script(scripts.Script):
    def title(self):
        return "(Gamma) frame_generator & video_generator"

    def show(self, is_img2img):
        return is_img2img

    def ui(self, is_img2img):

        gr.Markdown(""" 
        ## 视频生成'帧'/video2frame
        由视频生成帧,注意视频地址要具体到哪一个视频,需要文件名，path/to/video.mp4!!!! \\
        """)
        
        video_input_dir = gr.Textbox(label='Video Input directory', lines=1,placeholder='path/to/video.mp4')
        frame_output_dir = gr.Textbox(label='Frame Output directory', lines=1,placeholder='output/folder')
        btn = gr.Button(value="gene_frame")
        btn.click(video2frame, inputs=[video_input_dir, frame_output_dir])

        gr.Markdown(""" 
        ## 帧生成'视频'/frame2video
        由图片转化为视频，注意这里只需要给出生成视频的地址即可，不要文件名！！！！\\
        """)
        fps = gr.Slider(
            minimum=1,
            maximum=60,
            step=1,
            label='FPS',
            value=30,
            elem_id=self.elem_id("FPS"))
        frame_input_dir = gr.Textbox(label='Frame Input directory', lines=1,placeholder='input/folder')
        video_output_dir = gr.Textbox(label='Video Output directory', lines=1,placeholder='output/folder')
        btn1 = gr.Button(value="gene_video")
        btn1.click(frame2video, inputs=[frame_input_dir, video_output_dir,fps])