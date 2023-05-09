import torch



sample_z = torch.randn(1, 512)
growth_rate = 0.1

for i in range(10):
    # change the first dimension of sample_z
    sample_z[:, 1] += growth_rate
    print(sample_z[:, 1])
