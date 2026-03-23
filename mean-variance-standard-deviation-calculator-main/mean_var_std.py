import numpy as np

def calculate(list):
    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")
    
    mat=np.array((list)).reshape(3,3)
    # axis = 0 -> row wise (column same)
    # axis = 1 -> column wise (row same)
    # tolist() -> array to list
    # item() -> numpy number to regular number
    calculations= {
        'mean':[mat.mean(axis=0).tolist() , mat.mean(axis=1).tolist() , mat.mean().item()],
        'variance':[mat.var(axis=0).tolist() , mat.var(axis=1).tolist() , mat.var().item()],     
        'standard deviation':[mat.std(axis=0).tolist() , mat.std(axis=1).tolist() , mat.std().item()], 
        'max':[mat.max(axis=0).tolist() , mat.max(axis=1).tolist() , mat.max().item()],
        'min':[mat.min(axis=0).tolist() , mat.min(axis=1).tolist() , mat.min().item()],
        'sum':[mat.sum(axis=0).tolist() , mat.sum(axis=1).tolist() , mat.sum().item()],
        }
    return calculations