import numpy as np

from physion.visual_stim.main import vis_stim_image_built,\
        init_times_frames, init_bg_image

####################################
##  ----    CENTER GRATING --- #####
####################################

params = {"movie_refresh_freq":10,
          "presentation-duration":3,
          # stimulus parameters (add parenthesis with units):
          "x-center (deg)":0.,
          "y-center (deg)":0.,
          "size (deg)":4.,
          "angle (deg)":0,
          "radius (deg)":40.,
          "spatial-freq (cycle/deg)":0.04,
          "contrast (lum.)":1.0,
          "bg-color (lum.)":0.5}
    

class stim(vis_stim_image_built):
    """
    stimulus specific visual stimulation object

    all functions should accept a "parent" argument that can be the 
    multiprotocol holding this protocol
    """

    def __init__(self, protocol):

        super().__init__(protocol,
                         keys=['bg-color',
                               'x-center', 'y-center',
                               'radius','spatial-freq',
                               'angle', 'contrast'])

        ## /!\ inside here always use self.refresh_freq 
        ##        not the parent cls.refresh_freq 
        # when the parent multiprotocol will have ~10Hz refresh rate,
        ##                this can remain 2-3Hz
        self.refresh_freq = protocol['movie_refresh_freq']


    def get_image(self, episode, time_from_episode_start=0, parent=None):
        cls = (parent if parent is not None else self)
        img = init_bg_image(cls, episode)
        self.add_grating_patch(img,
                       angle=cls.experiment['angle'][episode],
                       radius=cls.experiment['radius'][episode],
                       spatial_freq=cls.experiment['spatial-freq'][episode],
                       contrast=cls.experiment['contrast'][episode],
                       xcenter=cls.experiment['x-center'][episode],
                       zcenter=cls.experiment['y-center'][episode])
        return img

    def plot_stim_picture(self, episode,
                          ax=None, parent=None, label=None, vse=False,
                          arrow={'length':10,
                                 'width_factor':0.05,
                                 'color':'red'}):

        cls = (parent if parent is not None else self)
        ax = self.show_frame(episode, ax=ax, label=label,
                             parent=parent)
        return ax
