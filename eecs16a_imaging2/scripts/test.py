import numpy as np

def testing(H, H_Alt):
  
    htest = ''
    halttest = ''
    if H.shape != (32*32, 32*32) or not np.isfinite(np.linalg.cond(H)):
        htest = 'H shape is incorrect'
    if H_Alt.shape != (32*32, 32*32) or not np.isfinite(np.linalg.cond(H_Alt)):
        halttest = 'H_Alt shape is incorrect, please fix'
    print(htest)
    print(halttest)
    if not htest and not halttest:
        print('Your matrix shapes are correct.')
