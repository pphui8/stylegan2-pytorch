1. prepare data
```bash
python prepare_data.py --out /root/autodl-tmp/pdata --size 256 /root/autodl-tmp/imgs
```

2. prepare a empty ./sample folder
3. train
```bash
python train.py --size 256 /root/autodl-tmp/pdata 2>&1 | tee /train.log
```
3. generate
```bash
python generate.py --sample 1 --pics 1000 --ckpt ./checkppoint/180000.pt
```
4. check the size of ./sample folder
```bash
du -s -m ./sample
```
