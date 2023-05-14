import torch
import torch.nn as nn

def create_mask(q, kv, query_size):
    n_q, c_q, h_q, w_q = q.shape
    n_kv, c_kv, h_kv, w_kv = kv.shape
    ratiao = h_kv/h_q
    x_grid, y_grid = torch.meshgrid(torch.arange(h_kv), torch.arange(h_kv))
    mask = []
    for i in  range(h_q * w_q):
        line = int(i // h_q * ratiao)
        row = int(i % h_q * ratiao)
        bound = query_size//2
        idx1 = torch.zeros_like(x_grid)
        idx2 = torch.zeros_like(y_grid)
        idx1[(line-bound <= x_grid) == (x_grid <= line+bound)] = 1
        idx2[(row-bound <= y_grid) == (y_grid <= row+bound)] = 1
        idx = idx1 + idx2
        idx = torch.where(idx==2 , torch.ones(h_kv, w_kv), torch.zeros(h_kv, w_kv))
        idx = idx.flatten(0).unsqueeze(0)
        mask.append(idx)
    mask = torch.cat(mask, dim=0)
    return mask==0