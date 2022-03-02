import pickle

class CaptureUtils(object):
    def __init__(self):
        self.outputs = []
    
    def __call__(self, result=None):
        if result is None:
            return
        self.outputs.append(result)
    
    def show(self):
        for idx,fig in enumerate(self.outputs):
            #fig = c.get_figure()
            #print(fig)
            #fig.set_size_inches(2, 2)
            #print('fig')
            display(fig)

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
    captureUtils.show()