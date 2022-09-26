""" Make image to move
"""

import numpy as np
import scipy.ndimage as snd

import nibabel as nib

import nipraxis

anat_fname = nipraxis.fetch_file('ds114_sub009_highres.nii')
img = nib.load(anat_fname)
data = img.get_fdata()

orig_slice = data[:, :, 160]

new_slice = snd.shift(orig_slice, [29, -5])

np.savetxt('original_slice.txt', orig_slice)
np.savetxt('moved_slice.txt', new_slice)

new_slice2 = snd.shift(orig_slice, [-15, 3])
np.savetxt('moved_slice2.txt', new_slice2)
