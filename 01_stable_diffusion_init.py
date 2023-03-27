%cd /content
%mkdir /content/video_src
%mkdir /content/video_out
!git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
%cd /content/stable-diffusion-webui
%cp /content/colaboratory/scripts/multi_frame_render_self.py /content/stable-diffusion-webui/scripts
%cp /content/colaboratory/scripts/multi_frame_rendering_self.py /content/stable-diffusion-webui/scripts
%cp /content/colaboratory/scripts/video2frame.py /content/stable-diffusion-webui/scripts
!python launch.py --share --xformers --enable-insecure-extension-access
