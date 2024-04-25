import numpy as np

def calculate(list):
    if(len(list)!=9):
        raise ValueError("List must contain nine numbers.")
   
    lst=np.array(list)

    rowmean=[lst[[0,1,2]].mean(), lst[[3,4,5]].mean(), lst[[6,7,8]].mean()]
    colmean=[lst[[0,3,6]].mean(), lst[[1,4,7]].mean(), lst[[2,5,8]].mean()]
    
    rowvar=[lst[[0,1,2]].var(), lst[[3,4,5]].var(), lst[[6,7,8]].var()]
    colvar=[lst[[0,3,6]].var(), lst[[1,4,7]].var(), lst[[2,5,8]].var()]
    
    rowmax=[lst[[0,1,2]].max(), lst[[3,4,5]].max(), lst[[6,7,8]].max()]
    colmax=[lst[[0,3,6]].max(), lst[[1,4,7]].max(), lst[[2,5,8]].max()]

    rowstd=[lst[[0,1,2]].std(), lst[[3,4,5]].std(), lst[[6,7,8]].std()]
    colstd=[lst[[0,3,6]].std(), lst[[1,4,7]].std(), lst[[2,5,8]].std()]

    rowmin=[lst[[0,1,2]].min(), lst[[3,4,5]].min(), lst[[6,7,8]].min()]
    colmin=[lst[[0,3,6]].min(), lst[[1,4,7]].min(), lst[[2,5,8]].min()]
    
    rowsum=[lst[[0,1,2]].sum(), lst[[3,4,5]].sum(), lst[[6,7,8]].sum()]
    colsum=[lst[[0,3,6]].sum(), lst[[1,4,7]].sum(), lst[[2,5,8]].sum()]
    return{
        'mean': [colmean, rowmean, lst.mean()],
        'variance': [colvar, rowvar, lst.var()],
        'standard deviation': [colstd, rowstd, lst.std()],
        'max': [colmax, rowmax, lst.max()],
        'min': [colmin, rowmin, lst.min()],
        'sum': [colsum, rowsum, lst.sum()]
    }