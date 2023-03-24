
%cd /content/stable-diffusion-webui/extensions
!git clone https://github.com/Mikubill/sd-webui-controlnet

%cd /content/stable-diffusion-webui/models/ControlNet
!git clone https://huggingface.co/lllyasviel/ControlNet/resolve/main/models/control_sd15_canny.pth
!git clone https://huggingface.co/lllyasviel/ControlNet/resolve/main/models/control_sd15_depth.pth
!git clone https://huggingface.co/lllyasviel/ControlNet/resolve/main/models/control_sd15_hed.pth
!git clone https://huggingface.co/lllyasviel/ControlNet/resolve/main/models/control_sd15_mlsd.pth
!git clone https://huggingface.co/lllyasviel/ControlNet/resolve/main/models/control_sd15_normal.pth
!git clone https://huggingface.co/lllyasviel/ControlNet/resolve/main/models/control_sd15_openpose.pth
!git clone https://huggingface.co/lllyasviel/ControlNet/resolve/main/models/control_sd15_scribble.pth
!git clone https://huggingface.co/lllyasviel/ControlNet/resolve/main/models/control_sd15_seg.pth
