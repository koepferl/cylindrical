import numpy as np

from hyperion.model import ModelOutput
from hyperion.util.constants import pc

# Open the model - we specify the name without the .rtout extension
m = ModelOutput('test_disc.rtout')

# Extract the SED for the smallest inclination and largest aperture, and
# scale to 300pc. In Python, negative indices can be used for lists and
# arrays, and indicate the position from the end. So to get the SED in the
# largest aperture, we set aperture=-1.
wav, nufnu = m.get_sed(inclination=9, aperture=-1, distance=300 * pc)

# Write out the SED to file
np.savetxt('sed.txt', zip(wav, nufnu), fmt="%11.4e %11.4e")