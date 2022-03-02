import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

class CaptureUtils(object):
    def __init__(self):
        self.outputs = []
        self.img_outputs = []
    
    #def __call__(self, result=None):
    #    if result is None:
    #        return
    #    self.outputs.append(result)

    def capture_imgs(self, imgs, titles=None):
        assert len(imgs.shape) == 4
        if titles is not None:
            assert imgs.shape[0] == len(titles)
        imgs = np.transpose(imgs, (0,2,3,1))
        B, H, W, C = imgs.shape
        for bidx in range(B):
            img = imgs[bidx]
            if titles is None:
                self.img_outputs.append((img,))
            else:
                title = titles[bidx]
                self.img_outputs.append((img, title))
    
    def show_imgs(self, ratio=2, n_rows=8):
        num_figures = len(self.img_outputs)
        n_cols = num_figures//n_rows+1
        fig_m = plt.figure(figsize=(ratio*n_rows, ratio*n_cols))
        gs = gridspec.GridSpec(n_cols, n_rows)#, wspace=0.1, hspace=0.2)
        for idx, obj in enumerate(self.img_outputs):
            ax = fig_m.add_subplot(gs[idx])
            if len(obj) == 2:
                img, title = obj
                ax.set_title(title)
                #ax.text(0.01, 0.01, title, style='italic',
                #bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
            else:
                img, = obj
            ax.imshow(img)
            ax.axis('off')
        plt.tight_layout()
        #plt.show()
        #display(fig_m)
        #fig.show()

    @classmethod
    def load(cls, name):
        with open(name, 'rb') as f:
            return pickle.load(f)

    def save(self, name='io.pkl'):
        with open(name, 'wb') as f:
            pickle.dump(self, f)

if __name__ == '__main__':
    #captureUtils = CaptureUtils()
    captureUtils = CaptureUtils.load('io.pkl')
    #captureUtils.load('io.pkl')
    #print(captureUtils.outputs)
    captureUtils.show_imgs()