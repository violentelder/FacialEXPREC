from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)
import sys
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
sys.path.append(os.path.dirname(__file__) + '/ui')
from ui import UI
from PyQt5 import QtWidgets


def load_cnn_model():
    """
    载入CNN模型
    :return:
    """
    from model import CNN
    model = CNN()
    model.load_weights('./models/cnn_best_weights.h5')
    return model


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QMainWindow()
    
    model = load_cnn_model()
    ui = UI(form, model)
    form.show()
    sys.exit(app.exec_())
