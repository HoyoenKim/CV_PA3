1. 구글 코랩에서 진행하였습니다. (Colab Pro+, A100 이용)

2. simple_unet.pth 는 coarse segmentation을 구하기 위한 unet입니다.

3. cspn_unet.pth 는 cspn segmentation을 구하기 위한 unet입니다. 2의 unet도 이 과정에서 학습되어서 simple_unet_with_cspn.pth에 저장됩니다.

4. 2 ~ 3을 imagenet을 이용하여 pretrain된 wieght을 이용하여 반복합니다.