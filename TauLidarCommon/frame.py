
from enum import Enum

class FrameType(Enum):
    '''
    FrameType Enum
    '''
    DISTANCE  = 0           ## frame with distance only
    DISTANCE_GRAYSCALE = 1  ## frame with distance and grayscale
    DISTANCE_AMPLITUDE = 2  ## frame with distance and amplitude

class Frame :
    '''
    3D Frame data including distance and grayscale.

    Attributes
    ----------
    height: 
        image height.
    width: 
        image width.
    data_depth: 
        depth map data, one dimensional array of float32. Example of converting to numpy array (opencv one channel Mat):
        mat_depth_map = np.frombuffer(frame.data_depth, dtype=np.float32, count=-1, offset=0).reshape(frame.height, frame.width)

    data_depth_rgb: 
        depth color map data, three dimensional array of uint8. Example of converting to numpy array (opencv three channel Mat):
        mat_depth_rgb = np.frombuffer(frame.data_depth_rgb, dtype=np.uint16, count=-1, offset=0).reshape(frame.height, frame.width, 3)
        mat_depth_rgb = mat_depth_rgb.astype(np.uint8)

    data_grayscale: 
        grayscale data, one dimensional array of uint8. Example of converting to numpy array (opencv one channel Mat):
        mat_grayscale = np.frombuffer(frame.data_grayscale, dtype=np.uint16, count=-1, offset=0).reshape(frame.height, frame.width)
        mat_grayscale = mat_grayscale.astype(np.uint8)

    data_amplitude: 
        amplitude data, one dimensional array of uint16. Example of converting to numpy array (opencv one channel Mat):
        mat_amplitude = np.frombuffer(frame.data_amplitude, dtype=np.float32, count=-1, offset=0).reshape(frame.height, frame.width)
        mat_amplitude = mat_amplitude.astype(np.uint8)

    points_3d: 
        3D points: list of unorganized 3D points. 
    '''
    def __init__(self, _height, _width, _data_depth, _data_depth_rgb, _data_grayscale, _data_amplitude, _points_3d, _data) :
        self.height           = _height
        self.width            = _width
        self.data_depth       = _data_depth
        self.data_depth_rgb   = _data_depth_rgb
        self.data_grayscale   = _data_grayscale
        self.data_amplitude   = _data_amplitude
        self.points_3d = _points_3d
        self._data = _data
