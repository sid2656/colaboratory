
%cd /content/stable-diffusion-webui/extensions
!git clone https://github.com/Mikubill/sd-webui-controlnet
%cd /content/stable-diffusion-webui
!python launch.py --share --xformers --enable-insecure-extension-access

