import numpy as np
def interpolate(wavelength, flux):
    "This function makes the interpolation and return the data to be plotted"
    n=3 #order of polynom
    wavelength,flux=np.array(wavelength), np.array(flux)
    dev=np.std(flux)
    index=(np.absolute(flux-flux.mean())<dev) & (flux<flux.mean())
    wave1=wavelength[index]
    flux1=flux[index]
    coeficients=np.polyfit(wave1,flux1,n)
    data=np.polyval(coeficients, wave1)
    return wave1,data