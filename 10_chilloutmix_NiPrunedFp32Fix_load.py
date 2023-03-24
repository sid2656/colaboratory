
echo "download chilloutmix model start ..."
%cd /content/stable-diffusion-webui/extensions
!wget https://huggingface.co/SakerLy/chilloutmix_NiPrunedFp32Fix/resolve/main/chilloutmix_NiPrunedFp32Fix.safetensors -O /content/stable-diffusion-webui/models/Stable-diffusion/chilloutmix_NiPrunedFp32Fix.safetensors
!wget https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors -O /content/stable-diffusion-webui/models/VAE/vae-ft-mse-840000-ema-pruned.safetensorsvae-ft-mse-840000-ema-pruned.safetensors
echo "download chilloutmix model end ..."
