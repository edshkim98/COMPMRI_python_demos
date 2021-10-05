import os
import numpy as np
import matplotlib.pyplot as plt


def ImageViewer(filename, dimensions, spacings, location):
    # Load data from file

    # get path of script
    script_dir = os.path.dirname(__file__)
    # create fileid
    fileid = open(os.path.join(script_dir,
                               filename), 'rb')
    # read data from file
    data = np.fromfile(fileid, dtype='<u1')

    # Convert data to 3D volume + create orthogonal slices

    # reshape data to match image dimensions, reorganise x y z dimensions
    volume = np.transpose(np.reshape(data, dimensions[::-1]), (2, 1, 0))
    # create axial slice
    axial = volume[:, :, location[2]]
    # create coronal slice
    coronal = np.squeeze(volume[:, location[1], :])
    # create sagittal slice
    sagittal = volume[location[0], :, :]

    # Plot results

    # generate figures and axes
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    axes = axes.ravel()
    fig.delaxes(axes[2])
    # axial slice
    axes[0].imshow(np.transpose(axial, (1, 0)),
                   extent=[0, volume.shape[0] * spacings[0],
                           0, volume.shape[1] * spacings[1]],
                   aspect=1,
                   origin='lower',
                   vmin=0,
                   vmax=255,
                   cmap='gray')
    axes[0].set_title('Axial')
    # coronal slice
    axes[1].imshow(np.transpose(coronal, (1, 0)),
                   extent=[0, volume.shape[0] * spacings[0],
                           0, volume.shape[2] * spacings[2]],
                   aspect=1,
                   origin='lower',
                   vmin=0,
                   vmax=255,
                   cmap='gray')
    axes[1].set_title('Coronal')
    # sagittal slice
    axes[3].imshow(np.transpose(sagittal, (1, 0)),
                   extent=[0, volume.shape[1] * spacings[1],
                           0, volume.shape[2] * spacings[2]],
                   aspect=1,
                   origin='lower',
                   vmin=0,
                   vmax=255,
                   cmap='gray')
    axes[3].set_title('Sagittal')

    # visualise figure
    plt.tight_layout()
    plt.show()
