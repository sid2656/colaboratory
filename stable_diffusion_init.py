!git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui

echo "download chilloutmix model start ..."
%cd /content/stable-diffusion-webui/extensions
!wget https://huggingface.co/SakerLy/chilloutmix_NiPrunedFp32Fix/resolve/main/chilloutmix_NiPrunedFp32Fix.safetensors -O /content/stable-diffusion-webui/models/Stable-diffusion/chilloutmix_NiPrunedFp32Fix.safetensors
!wget https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors -O /content/stable-diffusion-webui/models/VAE/vae-ft-mse-840000-ema-pruned.safetensorsvae-ft-mse-840000-ema-pruned.safetensors
echo "download chilloutmix model end ..."

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


%cd /content/stable-diffusion-webui
!python launch.py --share --xformers --enable-insecure-extension-access
