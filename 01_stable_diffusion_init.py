%cd /content
%mkdir /content/src
%mkdir /content/out
!git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
%cd /content/stable-diffusion-webui
%cp /content/colaboratory/scripts/multi_frame_render.py /content/stable-diffusion-webui/scripts
%cp /content/colaboratory/scripts/multi_frame_rendering.py /content/stable-diffusion-webui/scripts
%cp /content/colaboratory/scripts/video2frame.py /content/stable-diffusion-webui/scripts
!python launch.py --share --xformers --enable-insecure-extension-access
